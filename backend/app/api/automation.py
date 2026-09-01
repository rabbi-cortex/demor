"""Automation and settings routes."""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/automation")

class AutomationSettings(BaseModel):
    enabled: bool = True
    delay: int = 5

@router.get("/settings")
async def get_settings():
    return {"enabled": True, "delay": 5, "personality": "Professional"}

@router.patch("/settings")
async def update_settings(settings: AutomationSettings):
    return {"status": "updated"}
