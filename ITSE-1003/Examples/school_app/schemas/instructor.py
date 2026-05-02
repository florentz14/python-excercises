# -------------------------------------------------
# File Name: instructor.py
# Description: Pydantic schemas for Instructor (matches instructors table in school_db.sql)
# -------------------------------------------------

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class InstructorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)
    email: EmailStr
    bio: Optional[str] = None


class InstructorCreate(InstructorBase):
    pass


class InstructorUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=150)
    email: Optional[EmailStr] = None
    bio: Optional[str] = None


class InstructorResponse(InstructorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
