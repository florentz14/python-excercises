# -------------------------------------------------
# Business logic: instructors (soft delete, email único)
# -------------------------------------------------

from fastapi import HTTPException, status
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from models import Instructor
from schemas import InstructorCreate, InstructorUpdate


def _active_instructor_query(db: Session):
    return db.query(Instructor).filter(Instructor.deleted_at.is_(None))


def get_instructors(
    db: Session, skip: int = 0, limit: int = 100, search: str | None = None
) -> list[Instructor]:
    q = _active_instructor_query(db)
    if search:
        term = f"%{search.strip()}%"
        q = q.filter(sa_func.lower(Instructor.name).like(sa_func.lower(term)))
    return q.order_by(Instructor.id).offset(skip).limit(limit).all()


def get_instructor(db: Session, instructor_id: int) -> Instructor:
    obj = (
        _active_instructor_query(db)
        .filter(Instructor.id == instructor_id)
        .first()
    )
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Instructor not found"
        )
    return obj


def _email_taken(db: Session, email: str, exclude_id: int | None = None) -> bool:
    q = db.query(Instructor).filter(Instructor.email == email)
    if exclude_id is not None:
        q = q.filter(Instructor.id != exclude_id)
    return q.first() is not None


def create_instructor(db: Session, data: InstructorCreate) -> Instructor:
    email = str(data.email)
    if _email_taken(db, email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )
    obj = Instructor(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_instructor(
    db: Session, instructor_id: int, data: InstructorUpdate
) -> Instructor:
    obj = get_instructor(db, instructor_id)
    payload = data.model_dump(exclude_unset=True)
    if "email" in payload:
        email = str(payload["email"])
        if _email_taken(db, email, exclude_id=instructor_id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
    for field, value in payload.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def soft_delete_instructor(db: Session, instructor_id: int) -> None:
    obj = get_instructor(db, instructor_id)
    obj.deleted_at = sa_func.now()  # type: ignore[assignment]
    db.commit()
