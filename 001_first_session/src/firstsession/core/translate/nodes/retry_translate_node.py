# 목적: 재번역을 수행하는 노드를 정의한다.
# 설명: QC 실패 시 재시도 프롬프트로 번역을 복구한다.
# 디자인 패턴: 전략 패턴 + 파이프라인 노드
# 참조: docs/04_string_tricks/05_retry_logic.md

"""재번역 노드 모듈."""

from firstsession.core.translate.state.translation_state import TranslationState

from langchain_google_genai import ChatGoogleGenerativeAI
from firstsession.core.translate.prompts.retry_translate_prompt import RETRY_TRANSLATE_PROMPT


class RetryTranslateNode:
    """재번역을 담당하는 노드."""
    llm = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview",
            temperature=0.3,
        )

    def run(self, state: TranslationState) -> TranslationState:
        """재번역을 수행한다.
        Args:
            state: 현재 번역 상태.
        Returns:
            TranslationState: 재번역 결과가 포함된 상태.
        """
        # TODO: 재번역 프롬프트로 품질 개선 번역을 수행한다.
        source = state.get("normalized_text", "")
        failed_translation = state.get("translated_text", "")
        retry_count = state.get("retry_count", 0)
        prompt = RETRY_TRANSLATE_PROMPT.format(source_text=source, failed_translation=failed_translation)
        
        response = self.llm.invoke(prompt)
        improved_trans = response.text.strip()
        # TODO: 재번역 결과와 재시도 횟수를 갱신한다.
        state["translated_text"] = improved_trans
        state["retry_count"] = retry_count + 1
        return state
        #raise NotImplementedError("재번역 로직을 구현해야 합니다.")
