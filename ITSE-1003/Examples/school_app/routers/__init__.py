# -------------------------------------------------
# Routers exportados para main
# -------------------------------------------------

from .courses import router as courses_router
from .enrollments import router as enrollments_router
from .instructors import router as instructors_router
from .students import router as students_router

__all__ = [
    "students_router",
    "instructors_router",
    "courses_router",
    "enrollments_router",
]
