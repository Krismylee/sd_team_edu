# 목적: 번역 입력을 정규화하는 노드를 정의한다.
# 설명: 언어 코드와 텍스트를 기본 규칙으로 정리한다.
# 디자인 패턴: 파이프라인 노드
# 참조: firstsession/core/translate/graphs/translate_graph.py

"""입력 정규화 노드 모듈."""

from firstsession.core.translate.state.translation_state import TranslationState


class NormalizeInputNode:
    """입력 정규화를 담당하는 노드."""

    def run(self, state: TranslationState) -> TranslationState:
        """입력 데이터를 정규화한다.
        Args:
            state: 현재 번역 상태.

        Returns:
            TranslationState: 정규화된 상태.
        """
        source = state.get("source_language", "").lower()
        target = state.get("target_language", "").lower()
        text = state.get("text", "")
        
        state["source_language"] = self._language_normalize(source)
        state["target_language"] = self._language_normalize(target)
        state["normalized_text"] = self._text_normalize(text)
        
        return state
        
        
        # TODO: 언어 코드 표준화, 공백 정리, 길이 제한 규칙을 구현한다.
        # TODO: 금칙어/민감 정보 처리 기준을 정의한다.
    def _language_normalize(self, code: str) -> str:
        if not code:
            return ""
            
        code = code.split("-")[0] # ko-KR -> ko
        mapping = {
            "kr": "ko",
            "kor": "ko",
            "eng": "en"
        }
        return mapping.get(code, code)
        
    def _text_normalize(self, text: str) -> str:
        max_length = 5000
        if not text:
            return ""
        if len(text) > max_length:
            text = text[: max_length]
            text = text.strip()
            #text = re.sub(r"\s+", " ", text)
            
            
        return text
        
        #raise NotImplementedError("입력 정규화 로직을 구현해야 합니다.")
