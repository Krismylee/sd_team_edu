# firstSession

이 프로젝트는 FastAPI 기반의 기본 애플리케이션 진입점을 제공합니다.

## 실행 방법

아래 두 가지 방식 중 하나로 실행할 수 있습니다.

### 1) uvicorn CLI 방식 (권장)

```txt
uv run uvicorn firstSession.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2) 모듈 직접 실행 방식

```txt
uv run python -m firstSession.main
```

## 기본 엔드포인트

- 헬스 체크: `GET /health`

## 주요 위치

- 애플리케이션 진입점: `src/firstSession/main.py`
- API 영역: `src/firstSession/api`
- Core 영역: `src/firstSession/core`

## 환경 설정

프로젝트 루트에서 아래 순서로 실행하세요.

```txt
uv venv .venv
uv sync
```
