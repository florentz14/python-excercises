from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import AlbumCreate, AlbumUpdate, AlbumOut, AlbumDetail
from app import services

router = APIRouter(prefix="/albums", tags=["Albums"])


@router.get("/", response_model=list[AlbumOut])
def list_albums(
    skip: int = 0,
    limit: int = 50,
    artist_id: int | None = Query(None, description="Filter by artist"),
    db: Session = Depends(get_db),
):
    """List all albums, optionally filtered by artist."""
    return services.get_albums(db, skip, limit, artist_id)


@router.post("/", response_model=AlbumOut, status_code=status.HTTP_201_CREATED)
def create_album(data: AlbumCreate, db: Session = Depends(get_db)):
    """Create a new album."""
    return services.create_album(db, data)


@router.get("/{album_id}", response_model=AlbumDetail)
def get_album(album_id: int, db: Session = Depends(get_db)):
    """Get an album with its artist and song list."""
    return services.get_album(db, album_id)


@router.patch("/{album_id}", response_model=AlbumOut)
def update_album(album_id: int, data: AlbumUpdate, db: Session = Depends(get_db)):
    """Partially update an album."""
    return services.update_album(db, album_id, data)


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    """Delete an album and its songs (cascade)."""
    services.delete_album(db, album_id)
