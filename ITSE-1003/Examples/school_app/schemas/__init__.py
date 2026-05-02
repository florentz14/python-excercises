# -------------------------------------------------
# File Name: __init__.py
# Description: Pydantic schemas package for school app
# -------------------------------------------------

from .student import StudentCreate, StudentResponse, StudentUpdate
from .course import CourseCreate, CourseResponse, CourseUpdate
from .instructor import InstructorCreate, InstructorResponse, InstructorUpdate
from .enrollment import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate

__all__ = [
    "StudentCreate",
    "StudentResponse",
    "StudentUpdate",
    "CourseCreate",
    "CourseResponse",
    "CourseUpdate",
    "InstructorCreate",
    "InstructorResponse",
    "InstructorUpdate",
    "EnrollmentCreate",
    "EnrollmentResponse",
    "EnrollmentUpdate",
]
