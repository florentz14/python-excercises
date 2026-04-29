from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.artist import Artist
    from app.models.song import Song


class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    release_date: Mapped[datetime | None] = mapped_column(Date, nullable=True)
    cover_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    total_tracks: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    artist_id: Mapped[int] = mapped_column(
        ForeignKey("artists.id", ondelete="CASCADE"), nullable=False
    )
    artist: Mapped["Artist"] = relationship("Artist", back_populates="albums")
    songs: Mapped[list["Song"]] = relationship(
        "Song", back_populates="album", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Album(id={self.id}, title={self.title!r})>"
