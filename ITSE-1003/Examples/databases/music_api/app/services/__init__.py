from app.services.album_service import create_album, delete_album, get_album, get_albums, update_album
from app.services.artist_service import (
    create_artist,
    delete_artist,
    get_artist,
    get_artists,
    update_artist,
)
from app.services.genre_service import create_genre, delete_genre, get_genre, get_genres, update_genre
from app.services.song_service import (
    create_song,
    delete_song,
    get_song,
    get_songs,
    increment_play_count,
    update_song,
)

__all__ = [
    "get_genres",
    "get_genre",
    "create_genre",
    "update_genre",
    "delete_genre",
    "get_artists",
    "get_artist",
    "create_artist",
    "update_artist",
    "delete_artist",
    "get_albums",
    "get_album",
    "create_album",
    "update_album",
    "delete_album",
    "get_songs",
    "get_song",
    "create_song",
    "update_song",
    "delete_song",
    "increment_play_count",
]
