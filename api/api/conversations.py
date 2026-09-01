"""Conversations routes."""
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.models.models import User
from app.services.ai_service import AIService
from pydantic import BaseModel

router = APIRouter(prefix="/conversations")
ai_service = AIService()

class GenerationRequest(BaseModel):
    message: str
    history: list = []
    personality: str = "Professional"

@router.post("/{conversation_id}/generate-reply")
async def generate_reply(conversation_id: str, request: GenerationRequest, user: User = Depends(get_current_user)):
    return await ai_service.generate_response(
        conversation_id, request.message, request.history, request.personality
    )
