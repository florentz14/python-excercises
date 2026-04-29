from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import GenreCreate, GenreUpdate, GenreOut
from app import services

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.get("/", response_model=list[GenreOut])
def list_genres(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    """List all genres."""
    return services.get_genres(db, skip, limit)


@router.post("/", response_model=GenreOut, status_code=status.HTTP_201_CREATED)
def create_genre(data: GenreCreate, db: Session = Depends(get_db)):
    """Create a new genre."""
    return services.create_genre(db, data)


@router.get("/{genre_id}", response_model=GenreOut)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    """Get a genre by ID."""
    return services.get_genre(db, genre_id)


@router.patch("/{genre_id}", response_model=GenreOut)
def update_genre(genre_id: int, data: GenreUpdate, db: Session = Depends(get_db)):
    """Partially update a genre."""
    return services.update_genre(db, genre_id, data)


@router.delete("/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    """Delete a genre."""
    services.delete_genre(db, genre_id)
