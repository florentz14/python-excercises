from app.models.album import Album
from app.models.artist import Artist
from app.models.associations import song_artist_table, song_genre_table
from app.models.genre import Genre
from app.models.song import Song

__all__ = [
    "Artist",
    "Album",
    "Song",
    "Genre",
    "song_artist_table",
    "song_genre_table",
]
