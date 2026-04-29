from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import SongCreate, SongUpdate, SongOut, SongDetail
from app import services

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get("/", response_model=list[SongOut])
def list_songs(
    skip: int = 0,
    limit: int = 50,
    album_id: int | None = Query(None, description="Filter by album"),
    search: str | None = Query(None, description="Search by title"),
    db: Session = Depends(get_db),
):
    """List songs with optional filters."""
    return services.get_songs(db, skip, limit, album_id, search)


@router.post("/", response_model=SongDetail, status_code=status.HTTP_201_CREATED)
def create_song(data: SongCreate, db: Session = Depends(get_db)):
    """Create a new song. Accepts artist_ids and genre_ids arrays."""
    return services.create_song(db, data)


@router.get("/{song_id}", response_model=SongDetail)
def get_song(song_id: int, db: Session = Depends(get_db)):
    """Get a song with full details (album, artists, genres)."""
    return services.get_song(db, song_id)


@router.patch("/{song_id}", response_model=SongDetail)
def update_song(song_id: int, data: SongUpdate, db: Session = Depends(get_db)):
    """Partially update a song."""
    return services.update_song(db, song_id, data)


@router.delete("/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_song(song_id: int, db: Session = Depends(get_db)):
    """Delete a song."""
    services.delete_song(db, song_id)


@router.post("/{song_id}/play", response_model=SongOut)
def play_song(song_id: int, db: Session = Depends(get_db)):
    """Increment the play count of a song."""
    return services.increment_play_count(db, song_id)
