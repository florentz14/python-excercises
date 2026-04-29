from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Album
from app.schemas import AlbumCreate, AlbumUpdate
from app.services.artist_service import get_artist


def get_albums(db: Session, skip: int = 0, limit: int = 50, artist_id: int | None = None) -> list[Album]:
    q = db.query(Album)
    if artist_id:
        q = q.filter(Album.artist_id == artist_id)
    return q.offset(skip).limit(limit).all()


def get_album(db: Session, album_id: int) -> Album:
    obj = db.get(Album, album_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")
    return obj


def create_album(db: Session, data: AlbumCreate) -> Album:
    get_artist(db, data.artist_id)
    obj = Album(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_album(db: Session, album_id: int, data: AlbumUpdate) -> Album:
    obj = get_album(db, album_id)
    payload = data.model_dump(exclude_none=True)
    if "artist_id" in payload:
        get_artist(db, payload["artist_id"])
    for field, value in payload.items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_album(db: Session, album_id: int) -> None:
    obj = get_album(db, album_id)
    db.delete(obj)
    db.commit()
