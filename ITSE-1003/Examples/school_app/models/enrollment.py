# -------------------------------------------------
# File Name: enrollment.py
# Author: Florentino
# Date: 5/2/26
# Description: Enrollment model for school app (matches school_db.sql)
# -------------------------------------------------

from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Enrollment(Base):
    """
    Enrollment model representing student enrollments in courses
    Matches the enrollments table in school_db.sql
    """
    __tablename__ = "enrollments"

    id = Column(BigInteger, primary_key=True, index=True)
    student_id = Column(BigInteger, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, index=True)
    course_id = Column(BigInteger, ForeignKey("courses.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False, index=True)
    grade = Column(Numeric(5, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    student = relationship("Student", backref="enrollments")
    course = relationship("Course", backref="enrollments")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, grade={self.grade})>"

    def to_dict(self):
        """
        Convert enrollment object to dictionary
        """
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "grade": float(self.grade) if self.grade is not None else None,  # type: ignore
            "created_at": self.created_at.isoformat() if self.created_at is not None else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at is not None else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at is not None else None,
        }
