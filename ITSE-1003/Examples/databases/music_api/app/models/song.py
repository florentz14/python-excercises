from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.associations import song_artist_table, song_genre_table

if TYPE_CHECKING:
    from app.models.album import Album
    from app.models.artist import Artist
    from app.models.genre import Genre


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    track_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    lyrics: Mapped[str | None] = mapped_column(Text, nullable=True)
    play_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    album_id: Mapped[int | None] = mapped_column(
        ForeignKey("albums.id", ondelete="SET NULL"), nullable=True
    )
    album: Mapped["Album | None"] = relationship("Album", back_populates="songs")

    genres: Mapped[list["Genre"]] = relationship(
        secondary=song_genre_table, back_populates="songs"
    )
    artists: Mapped[list["Artist"]] = relationship(
        secondary=song_artist_table, back_populates="songs"
    )

    def __repr__(self) -> str:
        return f"<Song(id={self.id}, title={self.title!r})>"
