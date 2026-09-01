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
