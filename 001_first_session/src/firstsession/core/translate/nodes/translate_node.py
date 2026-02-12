# 목적: 번역을 수행하는 노드를 정의한다.
# 설명: 프롬프트 생성과 모델 호출을 포함할 수 있다.
# 디자인 패턴: 전략 패턴 + 파이프라인 노드
# 참조: docs/04_string_tricks/05_retry_logic.md

"""번역 수행 노드 모듈."""

from firstsession.core.translate.state.translation_state import TranslationState

#from langchain_google_genai import ChatGoogleGenerativeAI
from firstsession.core.translate.prompts.translation_prompt import TRANSLATION_PROMPT
from firstsession.core.translate.nodes.call_model_node import CallModelNode


class TranslateNode:
    """번역 수행을 담당하는 노드."""
    #llm = ChatGoogleGenerativeAI(
    #model="gemini-3-flash-preview",
    #temperature=0.3,  # 번역은 약간의 다양성 허용 가능
    #)


    def run(self, state: TranslationState) -> TranslationState:
        """번역 결과를 생성한다.
        Args:
            state: 현재 번역 상태.
        Returns:
            TranslationState: 번역 결과가 포함된 상태.
        """
        # TODO: 번역 프롬프트를 구성하고 모델/외부 API를 호출한다.
        source = state.get("source_language", "")
        target = state.get("target_language", "")
        text = state.get("normalized_text", "")
        
        prompt = TRANSLATION_PROMPT.format(source_language=source, target_language=target, text=text)
        
        
        self.call_model_node = CallModelNode()
        response = self.call_model_node.run(prompt, 0.3)
        #response = self.llm.invoke(prompt)
        translated = response.text.strip()
        
        state["translated_text"] = translated
        return state
        
        # TODO: 번역 결과를 상태에 기록하는 규칙을 정의한다.
        raise NotImplementedError("번역 수행 로직을 구현해야 합니다.")
