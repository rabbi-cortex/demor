"""SQLAlchemy Models."""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Float, ForeignKey, JSON, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    business_name = Column(String)
    business_description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    automation_settings = relationship("AutomationSettings", back_populates="user", uselist=False)
    business_hours = relationship("BusinessHours", back_populates="user")
    customers = relationship("Customer", back_populates="user")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    name = Column(String)
    email = Column(String)
    phone = Column(String, nullable=True)
    location = Column(String, nullable=True)
    status = Column(String, default="active") # active/inactive
    tags = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="customers")
    conversations = relationship("Conversation", back_populates="customer")

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    customer_id = Column(String, ForeignKey("customers.id"))
    status = Column(String, default="open") # open/resolved/pending
    assigned_to = Column(String, nullable=True)
    subject = Column(String)
    last_message_at = Column(DateTime, default=datetime.utcnow)
    unread_count = Column(Integer, default=0)
    ai_handled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")

class Message(Base):
    __tablename__ = "messages"
    id = Column(String, primary_key=True, default=generate_uuid)
    conversation_id = Column(String, ForeignKey("conversations.id"))
    sender_type = Column(String) # customer/ai/agent
    content = Column(String)
    ai_generated = Column(Boolean, default=False)
    ai_confidence = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")

class AutomationSettings(Base):
    __tablename__ = "automation_settings"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), unique=True)
    enabled = Column(Boolean, default=True)
    response_delay = Column(Integer, default=5)
    ai_personality = Column(String, default="Professional")
    language = Column(String, default="English")
    escalation_enabled = Column(Boolean, default=True)
    confidence_threshold = Column(Float, default=0.7)
    away_message = Column(String, default="Thanks for contacting us. We'll be back soon.")

    user = relationship("User", back_populates="automation_settings")

class BusinessHours(Base):
    __tablename__ = "business_hours"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    day_of_week = Column(Integer) # 0-6
    is_open = Column(Boolean, default=True)
    open_time = Column(String, default="09:00")
    close_time = Column(String, default="18:00")

    user = relationship("User", back_populates="business_hours")

class Integration(Base):
    __tablename__ = "integrations"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    platform = Column(String)
    status = Column(String, default="connected")
    config = Column(JSON, default=dict)
    webhook_url = Column(String, nullable=True)

class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"))
    source = Column(String)
    payload = Column(JSON)
    status = Column(String, default="pending")
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
