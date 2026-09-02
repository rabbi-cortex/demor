from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.api.deps import get_current_user
from api.core.database import get_db
from api.models.models import User, Integration
from api.schemas.schemas import IntegrationCreate, IntegrationResponse
from typing import List

router = APIRouter(prefix="/integrations")

@router.get("/", response_model=List[IntegrationResponse])
async def list_integrations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Integration).filter(Integration.user_id == current_user.id))
    return result.scalars().all()

@router.post("/", response_model=IntegrationResponse)
async def create_integration(
    integration: IntegrationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_integration = Integration(**integration.model_dump(), user_id=current_user.id)
    db.add(new_integration)
    await db.commit()
    await db.refresh(new_integration)
    return new_integration
