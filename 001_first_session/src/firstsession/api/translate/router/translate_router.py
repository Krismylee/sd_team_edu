# 목적: 번역 API 라우터를 제공한다.
# 설명: /api/v1/translate 경로에 번역 엔드포인트를 등록한다.
# 디자인 패턴: 라우터 팩토리 패턴
# 참조: firstsession/api/translate/const/api.py

"""번역 API 라우터 모듈."""

from fastapi import APIRouter

from firstsession.api.translate.const.api import (
    API_V1_PREFIX,
    TRANSLATE_PREFIX,
    TRANSLATE_TAG,
)
from firstsession.api.translate.model.translation_request import TranslationRequest
from firstsession.api.translate.model.translation_response import TranslationResponse
from firstsession.api.translate.service.translation_service import TranslationService


class TranslateRouter:
    """번역 API 라우터를 구성한다."""

    def __init__(self, service: TranslationService) -> None:
        """라우터와 의존성을 초기화한다.
        Args:
            service: 번역 서비스.
        """
        # 라우터 초기화 : prefix와 tag는 import됨
        self.router = APIRouter(
            prefix=f"{API_V1_PREFIX}{TRANSLATE_PREFIX}",
            tags=[TRANSLATE_TAG]
        )
        # 앤드포인트 등록
        self.router.add_api_route(
            path = "", # 라우터 prefx만 사용하므로 최종 url은 ""-> /api/v1/translate (router초기화 시 prefix와 tags로 정의됨)
            endpoint = self.translate,
            methods=["POST"],
            response_model=TranslationResponse
        )
        # 의존성 초기화 : TranslationService를 외부에서 주입받으므로 위임
        self.service = service
        
        #raise NotImplementedError("라우터 초기화 로직을 구현해야 합니다.")

    def translate(self, request: TranslationRequest) -> TranslationResponse:
        """번역 요청을 처리한다.
        Args:
            request: 번역 요청 데이터.

        Returns:
            TranslationResponse: 번역 결과.
        """
        result = self.service.translate(request)
        return TranslationResponse(**result)
    
        
        #raise NotImplementedError("번역 API 처리 로직을 구현해야 합니다.")
