from fastapi import APIRouter

from app.api.v1.endpoints import chat, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(chat.router, tags=["chat"])

# Future routers (Phase 2+):
# customers, leads, conversations, messages, qualification,
# assignment, follow_ups, notifications
