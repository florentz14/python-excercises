from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Song
from app.schemas import SongCreate, SongUpdate
from app.services.album_service import get_album
from app.services.artist_service import get_artist
from app.services.genre_service import get_genre


def _resolve_relations(db: Session, obj: Song, artist_ids: list[int] | None, genre_ids: list[int] | None) -> None:
    if artist_ids is not None:
        obj.artists = [get_artist(db, artist_id) for artist_id in artist_ids]
    if genre_ids is not None:
        obj.genres = [get_genre(db, genre_id) for genre_id in genre_ids]


def get_songs(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    album_id: int | None = None,
    search: str | None = None,
) -> list[Song]:
    q = db.query(Song)
    if album_id:
        q = q.filter(Song.album_id == album_id)
    if search:
        q = q.filter(Song.title.ilike(f"%{search}%"))
    return q.offset(skip).limit(limit).all()


def get_song(db: Session, song_id: int) -> Song:
    obj = db.get(Song, song_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return obj


def create_song(db: Session, data: SongCreate) -> Song:
    if data.album_id:
        get_album(db, data.album_id)

    payload = data.model_dump(exclude={"artist_ids", "genre_ids"})
    obj = Song(**payload)
    db.add(obj)
    db.flush()

    _resolve_relations(db, obj, data.artist_ids, data.genre_ids)

    db.commit()
    db.refresh(obj)
    return obj


def update_song(db: Session, song_id: int, data: SongUpdate) -> Song:
    obj = get_song(db, song_id)
    payload = data.model_dump(exclude_none=True)

    artist_ids = payload.pop("artist_ids", None)
    genre_ids = payload.pop("genre_ids", None)

    if "album_id" in payload and payload["album_id"]:
        get_album(db, payload["album_id"])

    for field, value in payload.items():
        setattr(obj, field, value)

    _resolve_relations(db, obj, artist_ids, genre_ids)

    db.commit()
    db.refresh(obj)
    return obj


def delete_song(db: Session, song_id: int) -> None:
    obj = get_song(db, song_id)
    db.delete(obj)
    db.commit()


def increment_play_count(db: Session, song_id: int) -> Song:
    obj = get_song(db, song_id)
    obj.play_count += 1
    db.commit()
    db.refresh(obj)
    return obj
