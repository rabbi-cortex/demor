from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.api.deps import get_current_user
from api.core.database import get_db
from api.models.models import User, AutomationSettings
from api.schemas.schemas import AutomationSettingsResponse, AutomationSettingsUpdate

router = APIRouter(prefix="/automation")

@router.get("/settings", response_model=AutomationSettingsResponse)
async def get_automation_settings(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(AutomationSettings).filter(AutomationSettings.user_id == current_user.id))
    settings = result.scalars().first()
    if not settings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Settings not found")
    return settings

@router.patch("/settings", response_model=AutomationSettingsResponse)
async def update_automation_settings(
    settings_update: AutomationSettingsUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(AutomationSettings).filter(AutomationSettings.user_id == current_user.id))
    settings = result.scalars().first()
    if not settings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Settings not found")

    for field, value in settings_update.model_dump(exclude_unset=True).items():
        setattr(settings, field, value)

    await db.commit()
    await db.refresh(settings)
    return settings
