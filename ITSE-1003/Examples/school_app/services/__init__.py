# -------------------------------------------------
# Re-export service functions (patrón music_api)
# -------------------------------------------------

from .course_service import (
    create_course,
    get_course,
    get_courses,
    soft_delete_course,
    update_course,
)
from .enrollment_service import (
    create_enrollment,
    get_enrollment,
    get_enrollments,
    soft_delete_enrollment,
    update_enrollment,
)
from .instructor_service import (
    create_instructor,
    get_instructor,
    get_instructors,
    soft_delete_instructor,
    update_instructor,
)
from .student_service import (
    create_student,
    get_student,
    get_students,
    soft_delete_student,
    update_student,
)

__all__ = [
    "get_students",
    "get_student",
    "create_student",
    "update_student",
    "soft_delete_student",
    "get_instructors",
    "get_instructor",
    "create_instructor",
    "update_instructor",
    "soft_delete_instructor",
    "get_courses",
    "get_course",
    "create_course",
    "update_course",
    "soft_delete_course",
    "get_enrollments",
    "get_enrollment",
    "create_enrollment",
    "update_enrollment",
    "soft_delete_enrollment",
]
