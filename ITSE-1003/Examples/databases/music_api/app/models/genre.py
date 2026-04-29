from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.associations import song_genre_table

if TYPE_CHECKING:
    from app.models.song import Song


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    songs: Mapped[list["Song"]] = relationship(
        secondary=song_genre_table, back_populates="genres"
    )

    def __repr__(self) -> str:
        return f"<Genre(id={self.id}, name={self.name!r})>"
