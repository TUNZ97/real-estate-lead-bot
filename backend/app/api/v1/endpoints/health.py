from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def api_health() -> dict:
    """API-prefixed health check."""
    return {"status": "ok"}
