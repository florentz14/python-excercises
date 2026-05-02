# -------------------------------------------------
# File Name: course.py
# Author: Florentino
# Date: 5/2/26
# Description: Course model for school app (matches school_db.sql)
# -------------------------------------------------

from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Course(Base):
    """
    Course model representing courses in the school
    Matches the courses table in school_db.sql
    """
    __tablename__ = "courses"

    id = Column(BigInteger, primary_key=True, index=True)
    course_name = Column(String(200), nullable=False, index=True)
    instructor_id = Column(BigInteger, ForeignKey("instructors.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    instructor = relationship("Instructor", backref="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, course_name='{self.course_name}', instructor_id={self.instructor_id})>"

    def to_dict(self):
        """
        Convert course object to dictionary
        """
        return {
            "id": self.id,
            "course_name": self.course_name,
            "instructor_id": self.instructor_id,
            "created_at": self.created_at.isoformat() if self.created_at is not None else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at is not None else None,
        }
