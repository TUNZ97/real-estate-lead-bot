from fastapi import APIRouter, Header
from pydantic import BaseModel, Field
from typing import Optional
import uuid

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    conversation_id: Optional[str] = None
    customer_id: Optional[str] = None


class ChatResponseData(BaseModel):
    conversation_id: str
    lead_id: Optional[str] = None
    response: str
    processing_status: str


class ChatResponse(BaseModel):
    data: ChatResponseData
    meta: dict = {}


@router.post("/chat", response_model=ChatResponse)
def post_chat(
    body: ChatRequest,
    x_request_id: Optional[str] = Header(default=None, alias="X-Request-ID"),
    idempotency_key: Optional[str] = Header(default=None, alias="Idempotency-Key"),
) -> ChatResponse:
    """
    Receive a customer message and return a bot response.

    Phase 0/2 placeholder: returns a static acknowledgement.
    Later phases will validate, call n8n, persist, and qualify.
    """
    conversation_id = body.conversation_id or str(uuid.uuid4())
    request_id = x_request_id or str(uuid.uuid4())

    return ChatResponse(
        data=ChatResponseData(
            conversation_id=conversation_id,
            lead_id=None,
            response=(
                "Thank you for your enquiry. Our lead system is being set up. "
                "A real assistant response will appear here once AI and workflows are connected."
            ),
            processing_status="PLACEHOLDER",
        ),
        meta={
            "request_id": request_id,
            "idempotency_key": idempotency_key,
        },
    )
