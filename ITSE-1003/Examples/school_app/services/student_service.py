# -------------------------------------------------
# Business logic: students (soft delete, email único)
# -------------------------------------------------

from fastapi import HTTPException, status
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from models import Student
from schemas import StudentCreate, StudentUpdate


def _active_student_query(db: Session):
    return db.query(Student).filter(Student.deleted_at.is_(None))


def get_students(
    db: Session, skip: int = 0, limit: int = 100, search: str | None = None
) -> list[Student]:
    q = _active_student_query(db)
    if search:
        term = f"%{search.strip()}%"
        q = q.filter(sa_func.lower(Student.name).like(sa_func.lower(term)))
    return q.order_by(Student.id).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int) -> Student:
    obj = (
        _active_student_query(db)
        .filter(Student.id == student_id)
        .first()
    )
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return obj


def _email_taken(db: Session, email: str, exclude_id: int | None = None) -> bool:
    q = db.query(Student).filter(Student.email == email)
    if exclude_id is not None:
        q = q.filter(Student.id != exclude_id)
    return q.first() is not None


def create_student(db: Session, data: StudentCreate) -> Student:
    email = str(data.email)
    if _email_taken(db, email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
    obj = Student(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_student(db: Session, student_id: int, data: StudentUpdate) -> Student:
    obj = get_student(db, student_id)
    payload = data.model_dump(exclude_unset=True)
    if "email" in payload:
        email = str(payload["email"])
        if _email_taken(db, email, exclude_id=student_id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
    for field, value in payload.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def soft_delete_student(db: Session, student_id: int) -> None:
    obj = get_student(db, student_id)
    obj.deleted_at = sa_func.now()  # type: ignore[assignment]
    db.commit()
