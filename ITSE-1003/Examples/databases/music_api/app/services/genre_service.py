from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Genre
from app.schemas import GenreCreate, GenreUpdate


def get_genres(db: Session, skip: int = 0, limit: int = 50) -> list[Genre]:
    return db.query(Genre).offset(skip).limit(limit).all()


def get_genre(db: Session, genre_id: int) -> Genre:
    obj = db.get(Genre, genre_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return obj


def create_genre(db: Session, data: GenreCreate) -> Genre:
    existing = db.query(Genre).filter(Genre.name == data.name).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Genre already exists")
    obj = Genre(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_genre(db: Session, genre_id: int, data: GenreUpdate) -> Genre:
    obj = get_genre(db, genre_id)
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_genre(db: Session, genre_id: int) -> None:
    obj = get_genre(db, genre_id)
    db.delete(obj)
    db.commit()
