"""Pydantic schemas for API requests and responses."""
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Any
from datetime import datetime
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    business_name: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    business_name: str

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: str
    user_id: str
    created_at: datetime

class ConversationResponse(BaseModel):
    id: str
    customer_id: str
    status: str
    subject: str
    last_message_at: datetime
    unread_count: int

class MessageCreate(BaseModel):
    content: str

class MessageResponse(BaseModel):
    id: str
    sender_type: str
    content: str
    created_at: datetime

class AutomationSettingsResponse(BaseModel):
    id: str
    user_id: str
    enabled: bool
    response_delay: int
    ai_personality: str
    language: str
    escalation_enabled: bool
    confidence_threshold: float
    away_message: str

class AutomationSettingsUpdate(BaseModel):
    enabled: Optional[bool] = None
    response_delay: Optional[int] = None
    ai_personality: Optional[str] = None
    language: Optional[str] = None
    escalation_enabled: Optional[bool] = None
    confidence_threshold: Optional[float] = None
    away_message: Optional[str] = None

class IntegrationBase(BaseModel):
    platform: str
    config: Any

class IntegrationCreate(IntegrationBase):
    pass

class IntegrationResponse(IntegrationBase):
    id: str
    user_id: str
    status: str
    webhook_url: Optional[str]
