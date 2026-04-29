from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ArtistCreate, ArtistUpdate, ArtistOut, ArtistDetail
from app import services

router = APIRouter(prefix="/artists", tags=["Artists"])


@router.get("/", response_model=list[ArtistOut])
def list_artists(
    skip: int = 0,
    limit: int = 50,
    search: str | None = Query(None, description="Filter by name (partial match)"),
    db: Session = Depends(get_db),
):
    """List all artists with optional name search."""
    return services.get_artists(db, skip, limit, search)


@router.post("/", response_model=ArtistOut, status_code=status.HTTP_201_CREATED)
def create_artist(data: ArtistCreate, db: Session = Depends(get_db)):
    """Create a new artist."""
    return services.create_artist(db, data)


@router.get("/{artist_id}", response_model=ArtistDetail)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    """Get an artist with their albums and songs."""
    return services.get_artist(db, artist_id)


@router.patch("/{artist_id}", response_model=ArtistOut)
def update_artist(artist_id: int, data: ArtistUpdate, db: Session = Depends(get_db)):
    """Partially update an artist."""
    return services.update_artist(db, artist_id, data)


@router.delete("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    """Delete an artist and all their albums/songs (cascade)."""
    services.delete_artist(db, artist_id)
