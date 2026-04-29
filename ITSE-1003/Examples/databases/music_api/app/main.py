from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routers import genres_router, artists_router, albums_router, songs_router

# Import models so SQLAlchemy registers them before create_all
import app.models  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables on startup
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown (nothing needed for SQLite dev)


app = FastAPI(
    title="🎵 Music Library API",
    description=(
        "CRUD completo para gestionar **Artistas**, **Álbumes**, **Canciones** y **Géneros** "
        "usando FastAPI + SQLAlchemy con relaciones M2M y N:1.\n\n"
        "### Características\n"
        "- Artistas con múltiples álbumes\n"
        "- Álbumes con múltiples canciones\n"
        "- Canciones con múltiples géneros y artistas (featuring)\n"
        "- Búsqueda y filtros en listados\n"
        "- Contador de reproducciones por canción"
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(genres_router)
app.include_router(artists_router)
app.include_router(albums_router)
app.include_router(songs_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "🎵 Music Library API",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "genres": "/genres",
            "artists": "/artists",
            "albums": "/albums",
            "songs": "/songs",
        },
    }
