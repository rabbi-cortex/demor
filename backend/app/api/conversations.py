"""Conversations routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.api.deps import get_current_user
from api.core.database import get_db
from api.models.models import User, Conversation
from api.schemas.schemas import ConversationResponse
from api.services.ai_service import AIService
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/conversations")
ai_service = AIService()

class GenerationRequest(BaseModel):
    message: str
    history: list = []
    personality: str = "Professional"

@router.get("/", response_model=List[ConversationResponse])
async def list_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Conversation).filter(Conversation.user_id == current_user.id))
    return result.scalars().all()

@router.get("/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == current_user.id))
    conversation = result.scalars().first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    return conversation

@router.patch("/{conversation_id}/status", response_model=ConversationResponse)
async def update_conversation_status(
    conversation_id: str,
    status_str: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == current_user.id))
    conversation = result.scalars().first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    conversation.status = status_str
    await db.commit()
    await db.refresh(conversation)
    return conversation

@router.post("/{conversation_id}/generate-reply")
async def generate_reply(conversation_id: str, request: GenerationRequest, user: User = Depends(get_current_user)):
    return await ai_service.generate_response(
        conversation_id, request.message, request.history, request.personality
    )
