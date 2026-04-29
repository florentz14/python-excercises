from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from app.schemas.album import AlbumOut
    from app.schemas.song import SongOut


class ArtistBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, examples=["The Beatles"])
    bio: str | None = None
    country: str | None = Field(None, max_length=100, examples=["United Kingdom"])
    birth_date: date | None = None
    is_active: bool = True


class ArtistCreate(ArtistBase):
    pass


class ArtistUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    bio: str | None = None
    country: str | None = None
    birth_date: date | None = None
    is_active: bool | None = None


class ArtistOut(ArtistBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


class ArtistDetail(ArtistOut):
    albums: list["AlbumOut"] = []
    songs: list["SongOut"] = []
