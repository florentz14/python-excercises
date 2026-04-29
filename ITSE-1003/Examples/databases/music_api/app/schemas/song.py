from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from app.schemas.album import AlbumOut
    from app.schemas.artist import ArtistOut
    from app.schemas.genre import GenreOut


class SongBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, examples=["Come Together"])
    duration_seconds: int | None = Field(None, ge=0, examples=[259])
    track_number: int | None = Field(None, ge=1)
    lyrics: str | None = None
    album_id: int | None = None
    artist_ids: list[int] = Field(default_factory=list, description="IDs of featured artists")
    genre_ids: list[int] = Field(default_factory=list, description="IDs of genres")


class SongCreate(SongBase):
    pass


class SongUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    duration_seconds: int | None = Field(None, ge=0)
    track_number: int | None = Field(None, ge=1)
    lyrics: str | None = None
    album_id: int | None = None
    artist_ids: list[int] | None = None
    genre_ids: list[int] | None = None


class SongOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    duration_seconds: int | None
    track_number: int | None
    play_count: int
    album_id: int | None
    created_at: datetime


class SongDetail(SongOut):
    album: "AlbumOut | None" = None
    artists: list["ArtistOut"] = []
    genres: list["GenreOut"] = []
    lyrics: str | None = None
