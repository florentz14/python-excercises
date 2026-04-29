from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Artist
from app.schemas import ArtistCreate, ArtistUpdate


def get_artists(db: Session, skip: int = 0, limit: int = 50, search: str | None = None) -> list[Artist]:
    q = db.query(Artist)
    if search:
        q = q.filter(Artist.name.ilike(f"%{search}%"))
    return q.offset(skip).limit(limit).all()


def get_artist(db: Session, artist_id: int) -> Artist:
    obj = db.get(Artist, artist_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
    return obj


def create_artist(db: Session, data: ArtistCreate) -> Artist:
    obj = Artist(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_artist(db: Session, artist_id: int, data: ArtistUpdate) -> Artist:
    obj = get_artist(db, artist_id)
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_artist(db: Session, artist_id: int) -> None:
    obj = get_artist(db, artist_id)
    db.delete(obj)
    db.commit()
