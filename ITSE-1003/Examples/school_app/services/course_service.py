# -------------------------------------------------
# Business logic: courses (soft delete, FK instructor opcional)
# -------------------------------------------------

from fastapi import HTTPException, status
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from models import Course, Instructor
from schemas import CourseCreate, CourseUpdate


def _active_course_query(db: Session):
    return db.query(Course).filter(Course.deleted_at.is_(None))


def get_courses(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    search: str | None = None,
    instructor_id: int | None = None,
) -> list[Course]:
    q = _active_course_query(db)
    if search:
        term = f"%{search.strip()}%"
        q = q.filter(sa_func.lower(Course.course_name).like(sa_func.lower(term)))
    if instructor_id is not None:
        q = q.filter(Course.instructor_id == instructor_id)
    return q.order_by(Course.id).offset(skip).limit(limit).all()


def get_course(db: Session, course_id: int) -> Course:
    obj = _active_course_query(db).filter(Course.id == course_id).first()
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    return obj


def _ensure_instructor_if_set(db: Session, instructor_id: int | None) -> None:
    if instructor_id is None:
        return
    inst = (
        db.query(Instructor)
        .filter(
            Instructor.id == instructor_id,
            Instructor.deleted_at.is_(None),
        )
        .first()
    )
    if inst is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Instructor not found or inactive",
        )


def create_course(db: Session, data: CourseCreate) -> Course:
    _ensure_instructor_if_set(db, data.instructor_id)
    obj = Course(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_course(db: Session, course_id: int, data: CourseUpdate) -> Course:
    obj = get_course(db, course_id)
    payload = data.model_dump(exclude_unset=True)
    if "instructor_id" in payload:
        _ensure_instructor_if_set(db, payload["instructor_id"])
    for field, value in payload.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def soft_delete_course(db: Session, course_id: int) -> None:
    obj = get_course(db, course_id)
    obj.deleted_at = sa_func.now()  # type: ignore[assignment]
    db.commit()
