"""Chat application service: validate → call n8n → return bot response."""

from typing import Optional
import uuid
import logging

from app.core.config import settings
from app.core.errors import AppError
from app.services.n8n_client import n8n_client

logger = logging.getLogger(__name__)

# Safe fallback when n8n is offline during local development
FALLBACK_RESPONSE = (
    "Thank you for contacting PrimeHomes Realty. "
    "We've received your message and a sales representative will follow up shortly. "
    "Could you share your preferred location and budget if you haven't already?"
)


async def process_chat_message(
    *,
    message: str,
    conversation_id: Optional[str] = None,
    customer_id: Optional[str] = None,
    request_id: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> dict:
    conversation_id = conversation_id or str(uuid.uuid4())
    request_id = request_id or str(uuid.uuid4())

    # Skip n8n if webhook is clearly unset / placeholder
    if not settings.N8N_WEBHOOK_URL or settings.N8N_WEBHOOK_URL.strip() in (
        "",
        "http://localhost:5678/webhook/customer-message",
    ):
        # Still try the default local webhook; if it fails, fall back
        pass

    try:
        result = await n8n_client.process_customer_message(
            message=message,
            conversation_id=conversation_id,
            customer_id=customer_id,
            request_id=request_id,
            idempotency_key=idempotency_key,
        )
        return {
            "conversation_id": result["conversation_id"],
            "lead_id": result.get("lead_id"),
            "response": result["response"],
            "processing_status": result.get("processing_status", "SUCCESS"),
            "request_id": request_id,
        }
    except AppError as exc:
        # In development, return a friendly fallback so UI testing can continue
        if settings.APP_ENV == "development" and settings.DEBUG:
            logger.warning(
                "n8n unavailable (%s); returning fallback response. request_id=%s",
                exc.message,
                request_id,
            )
            return {
                "conversation_id": conversation_id,
                "lead_id": None,
                "response": FALLBACK_RESPONSE,
                "processing_status": "FALLBACK",
                "request_id": request_id,
                "n8n_error": exc.message,
            }
        raise
