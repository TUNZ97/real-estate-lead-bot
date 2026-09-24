from typing import Optional
from fastapi import APIRouter, Header

from app.schemas.chat import ChatRequest, ChatResponse, ChatResponseData
from app.services.chat_service import process_chat_message

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def post_chat(
    body: ChatRequest,
    x_request_id: Optional[str] = Header(default=None, alias="X-Request-ID"),
    idempotency_key: Optional[str] = Header(default=None, alias="Idempotency-Key"),
) -> ChatResponse:
    """
    Receive a customer message and return the bot response.

    Flow: validate → n8n WF-001 → return response.
    In development, falls back to a safe message if n8n is offline.
    """
    result = await process_chat_message(
        message=body.message,
        conversation_id=body.conversation_id,
        customer_id=body.customer_id,
        request_id=x_request_id,
        idempotency_key=idempotency_key,
    )

    meta = {
        "request_id": result.get("request_id"),
        "idempotency_key": idempotency_key,
    }
    if result.get("n8n_error"):
        meta["n8n_error"] = result["n8n_error"]

    return ChatResponse(
        data=ChatResponseData(
            conversation_id=result["conversation_id"],
            lead_id=result.get("lead_id"),
            response=result["response"],
            processing_status=result["processing_status"],
        ),
        meta=meta,
    )
