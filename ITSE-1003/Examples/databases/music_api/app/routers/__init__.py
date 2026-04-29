from app.routers.albums import router as albums_router
from app.routers.artists import router as artists_router
from app.routers.genres import router as genres_router
from app.routers.songs import router as songs_router

__all__ = ["genres_router", "artists_router", "albums_router", "songs_router"]
