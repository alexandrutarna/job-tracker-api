# app/schemas.py - Pydantic models for request/response validation

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    name: str
    status: str
    result: Optional[str] = None

class JobCreate(JobBase):
    pass  # same fields as JobBase

class JobRead(JobBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Required for converting from SQLAlchemy object to JSON
