# -------------------------------------------------
# File Name: instructor.py
# Author: Florentino
# Date: 5/2/26
# Description: Instructor model for school app (matches school_db.sql)
# -------------------------------------------------

from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Instructor(Base):
    """
    Instructor model representing instructors in the school
    Matches the instructors table in school_db.sql
    """
    __tablename__ = "instructors"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<Instructor(id={self.id}, name='{self.name}', email='{self.email}')>"

    def to_dict(self):
        """
        Convert instructor object to dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "bio": self.bio,
            "created_at": self.created_at.isoformat() if self.created_at is not None else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at is not None else None,
        }
