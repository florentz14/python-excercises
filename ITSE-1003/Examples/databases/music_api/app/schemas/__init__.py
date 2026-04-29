from app.schemas.album import AlbumBase, AlbumCreate, AlbumDetail, AlbumOut, AlbumUpdate
from app.schemas.artist import ArtistBase, ArtistCreate, ArtistDetail, ArtistOut, ArtistUpdate
from app.schemas.genre import GenreBase, GenreCreate, GenreOut, GenreUpdate
from app.schemas.song import SongBase, SongCreate, SongDetail, SongOut, SongUpdate

ArtistDetail.model_rebuild()
AlbumDetail.model_rebuild()
SongDetail.model_rebuild()

__all__ = [
    "GenreBase",
    "GenreCreate",
    "GenreUpdate",
    "GenreOut",
    "ArtistBase",
    "ArtistCreate",
    "ArtistUpdate",
    "ArtistOut",
    "ArtistDetail",
    "AlbumBase",
    "AlbumCreate",
    "AlbumUpdate",
    "AlbumOut",
    "AlbumDetail",
    "SongBase",
    "SongCreate",
    "SongUpdate",
    "SongOut",
    "SongDetail",
]
