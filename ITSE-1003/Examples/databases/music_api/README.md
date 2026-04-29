# 🎵 Music Library API

CRUD completo con **FastAPI + SQLAlchemy 2.0** para gestionar:
Artistas • Álbumes • Canciones • Géneros

## Estructura del proyecto

```
music_api/
├── app/
│   ├── main.py          # Aplicación FastAPI + lifespan
│   ├── database.py      # Engine, SessionLocal, Base
│   ├── models/
│   │   ├── artist.py
│   │   ├── album.py
│   │   ├── song.py
│   │   ├── genre.py
│   │   └── __init__.py  # Exporta modelos y tablas M2M
│   ├── schemas/
│   │   ├── artist.py
│   │   ├── album.py
│   │   ├── song.py
│   │   ├── genre.py
│   │   └── __init__.py  # Exporta schemas (In/Out/Detail)
│   ├── services/
│   │   ├── artist_service.py
│   │   ├── album_service.py
│   │   ├── song_service.py
│   │   ├── genre_service.py
│   │   └── __init__.py  # Exporta lógica de negocio / CRUD
│   └── routers/
│       ├── artists.py
│       ├── albums.py
│       ├── songs.py
│       └── genres.py
└── seed.py              # Script para datos demo
```

## Instalación y ejecución

```bash
# 1. Instalar dependencias
pip install -r ../../../../requirements.txt

# 2. (Opcional) Cargar datos demo
python seed.py

# 3. Levantar el servidor
uvicorn app.main:app --reload

# 4. Abrir documentación interactiva
#    http://localhost:8000/docs
```

## Endpoints

### Géneros
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/genres/` | Listar géneros |
| POST | `/genres/` | Crear género |
| GET | `/genres/{id}` | Obtener género |
| PATCH | `/genres/{id}` | Actualizar género |
| DELETE | `/genres/{id}` | Eliminar género |

### Artistas
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/artists/?search=` | Listar / buscar artistas |
| POST | `/artists/` | Crear artista |
| GET | `/artists/{id}` | Obtener artista con álbumes y canciones |
| PATCH | `/artists/{id}` | Actualizar artista |
| DELETE | `/artists/{id}` | Eliminar artista (cascade) |

### Álbumes
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/albums/?artist_id=` | Listar / filtrar por artista |
| POST | `/albums/` | Crear álbum |
| GET | `/albums/{id}` | Obtener álbum con canciones |
| PATCH | `/albums/{id}` | Actualizar álbum |
| DELETE | `/albums/{id}` | Eliminar álbum (cascade) |

### Canciones
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/songs/?album_id=&search=` | Listar / filtrar |
| POST | `/songs/` | Crear canción (con artist_ids y genre_ids) |
| GET | `/songs/{id}` | Obtener canción completa |
| PATCH | `/songs/{id}` | Actualizar canción |
| DELETE | `/songs/{id}` | Eliminar canción |
| POST | `/songs/{id}/play` | Incrementar reproducciones |

## Relaciones del modelo

```
Artist (1) ──── (N) Album (1) ──── (N) Song
   │                                    │
   └──── (M2M) song_artist ────────────┘   (featuring)
                                       │
                              (M2M) song_genre ──── Genre
```
