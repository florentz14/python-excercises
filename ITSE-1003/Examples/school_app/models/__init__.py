# -------------------------------------------------
# File Name: __init__.py
# Author: Florentino
# Date: 5/2/26
# Description: Models package for school app (matches school_db.sql)
# -------------------------------------------------

from .student import Student
from .instructor import Instructor
from .course import Course
from .enrollment import Enrollment

__all__ = ["Student", "Instructor", "Course", "Enrollment"]
