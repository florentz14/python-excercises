from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from app.schemas.artist import ArtistOut
    from app.schemas.song import SongOut


class AlbumBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, examples=["Abbey Road"])
    release_date: date | None = None
    cover_url: str | None = Field(None, max_length=500)
    total_tracks: int = Field(0, ge=0)
    artist_id: int


class AlbumCreate(AlbumBase):
    pass


class AlbumUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    release_date: date | None = None
    cover_url: str | None = None
    total_tracks: int | None = Field(None, ge=0)
    artist_id: int | None = None


class AlbumOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    release_date: date | None
    cover_url: str | None
    total_tracks: int
    artist_id: int
    created_at: datetime


class AlbumDetail(AlbumOut):
    artist: "ArtistOut | None" = None
    songs: list["SongOut"] = []
