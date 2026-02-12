# 목적: 입력 문장을 안전 분류로 라우팅한다.
# 설명: PASS/PII/HARMFUL/PROMPT_INJECTION 라벨로 안전 여부를 판정한다.
# 디자인 패턴: 전략 패턴 + 파이프라인 노드
# 참조: docs/04_string_tricks/02_single_choice_파서.md

"""안전 분류 노드 모듈."""

from firstsession.core.translate.state.translation_state import TranslationState
# 추가된 import
from firstsession.core.translate.prompts.safeguard_prompt import SAFEGUARD_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI


class SafeguardClassifyNode:
    """안전 분류를 담당하는 노드."""
    labels = {
        "PASS",
        "PII",
        "HARMFUL",
        "PROMPT_INJECTION"
    }
    llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",  # 또는 gemini-1.5-pro
    temperature=0
    )
    def run(self, state: TranslationState) -> TranslationState:
        """입력에 대한 안전 라벨을 판정한다.
        Args:
            state: 현재 번역 상태.
        Returns:
            TranslationState: 안전 라벨이 포함된 상태.
        """
        # TODO: 안전 분류 프롬프트를 호출하고 PASS/PII/HARMFUL/PROMPT_INJECTION을 산출한다.
        text = state.get("normalized_text", "")
        prompt = SAFEGUARD_PROMPT.format(user_input=text)
        response = self.llm.invoke(prompt)
        
        # TODO: 출력 검증 및 정규화 규칙을 정의한다.
        '''
        content = response.content

        if isinstance(content, list):
            text = "".join(
                item["text"] if isinstance(item, dict) else str(item)
                for item in content
            )
        else:
            text = content

        raw_output = text.strip().upper()
        '''
        raw_output = response.text.strip().upper()
        if raw_output not in self.labels:
            raw_output = "HARMFUL"
        
        state["safeguard_label"] = raw_output
        
        return state
        
        #raise NotImplementedError("안전 분류 로직을 구현해야 합니다.")
