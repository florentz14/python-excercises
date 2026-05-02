# -------------------------------------------------
# Business logic: enrollments (soft delete, par estudiante-curso único)
# -------------------------------------------------

from fastapi import HTTPException, status
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from models import Course, Enrollment, Student
from schemas import EnrollmentCreate, EnrollmentUpdate


def _active_enrollment_query(db: Session):
    return db.query(Enrollment).filter(Enrollment.deleted_at.is_(None))


def get_enrollments(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    student_id: int | None = None,
    course_id: int | None = None,
) -> list[Enrollment]:
    q = _active_enrollment_query(db)
    if student_id is not None:
        q = q.filter(Enrollment.student_id == student_id)
    if course_id is not None:
        q = q.filter(Enrollment.course_id == course_id)
    return q.order_by(Enrollment.id).offset(skip).limit(limit).all()


def get_enrollment(db: Session, enrollment_id: int) -> Enrollment:
    obj = (
        _active_enrollment_query(db)
        .filter(Enrollment.id == enrollment_id)
        .first()
    )
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found"
        )
    return obj


def _active_student(db: Session, student_id: int) -> Student:
    s = (
        db.query(Student)
        .filter(Student.id == student_id, Student.deleted_at.is_(None))
        .first()
    )
    if s is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student not found or inactive",
        )
    return s


def _active_course(db: Session, course_id: int) -> Course:
    c = (
        db.query(Course)
        .filter(Course.id == course_id, Course.deleted_at.is_(None))
        .first()
    )
    if c is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course not found or inactive",
        )
    return c


def create_enrollment(db: Session, data: EnrollmentCreate) -> Enrollment:
    _active_student(db, data.student_id)
    _active_course(db, data.course_id)

    existing = (
        db.query(Enrollment)
        .filter(
            Enrollment.student_id == data.student_id,
            Enrollment.course_id == data.course_id,
        )
        .first()
    )
    if existing is not None:
        if existing.deleted_at is None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Student is already enrolled in this course",
            )
        # Reactivar fila soft-deleted (respeta UNIQUE en BD)
        for field, value in data.model_dump().items():
            setattr(existing, field, value)
        existing.deleted_at = None  # type: ignore[assignment]
        db.commit()
        db.refresh(existing)
        return existing

    obj = Enrollment(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_enrollment(
    db: Session, enrollment_id: int, data: EnrollmentUpdate
) -> Enrollment:
    obj = get_enrollment(db, enrollment_id)
    payload = data.model_dump(exclude_unset=True)
    new_sid = payload.get("student_id", obj.student_id)
    new_cid = payload.get("course_id", obj.course_id)
    if "student_id" in payload or "course_id" in payload:
        _active_student(db, new_sid)
        _active_course(db, new_cid)
        other = (
            db.query(Enrollment)
            .filter(
                Enrollment.student_id == new_sid,
                Enrollment.course_id == new_cid,
                Enrollment.id != enrollment_id,
                Enrollment.deleted_at.is_(None),
            )
            .first()
        )
        if other is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Another active enrollment already uses this student and course",
            )
    for field, value in payload.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def soft_delete_enrollment(db: Session, enrollment_id: int) -> None:
    obj = get_enrollment(db, enrollment_id)
    obj.deleted_at = sa_func.now()  # type: ignore[assignment]
    db.commit()
