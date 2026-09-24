from typing import Optional
from pydantic import BaseModel, Field


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
    meta: dict = Field(default_factory=dict)
