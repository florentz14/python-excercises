"""
seed.py — Populates the database with demo data.
Run: python seed.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine, Base
import app.models  # noqa: F401 — registers models
from app.models import Artist, Album, Song, Genre
from datetime import date

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # ── Genres ──
    rock = Genre(name="Rock", description="Guitar-driven genre")
    pop = Genre(name="Pop", description="Popular mainstream music")
    jazz = Genre(name="Jazz", description="Improvisation-based genre")
    electronic = Genre(name="Electronic", description="Synthesizer-based music")
    db.add_all([rock, pop, jazz, electronic])
    db.flush()

    # ── Artists ──
    beatles = Artist(
        name="The Beatles",
        bio="Legendary British rock band from Liverpool.",
        country="United Kingdom",
        birth_date=date(1960, 8, 17),
        is_active=False,
    )
    miles = Artist(
        name="Miles Davis",
        bio="Iconic American jazz musician and composer.",
        country="United States",
        birth_date=date(1926, 5, 26),
        is_active=False,
    )
    daft = Artist(
        name="Daft Punk",
        bio="French electronic music duo.",
        country="France",
        birth_date=date(1993, 1, 1),
        is_active=False,
    )
    db.add_all([beatles, miles, daft])
    db.flush()

    # ── Albums ──
    abbey = Album(
        title="Abbey Road",
        release_date=date(1969, 9, 26),
        total_tracks=17,
        artist_id=beatles.id,
    )
    kind_of_blue = Album(
        title="Kind of Blue",
        release_date=date(1959, 8, 17),
        total_tracks=5,
        artist_id=miles.id,
    )
    discovery = Album(
        title="Discovery",
        release_date=date(2001, 2, 26),
        total_tracks=14,
        artist_id=daft.id,
    )
    db.add_all([abbey, kind_of_blue, discovery])
    db.flush()

    # ── Songs ──
    songs_data = [
        Song(title="Come Together", duration_seconds=259, track_number=1, album_id=abbey.id, play_count=120),
        Song(title="Something", duration_seconds=182, track_number=2, album_id=abbey.id, play_count=95),
        Song(title="Here Comes the Sun", duration_seconds=185, track_number=7, album_id=abbey.id, play_count=200),
        Song(title="So What", duration_seconds=564, track_number=1, album_id=kind_of_blue.id, play_count=80),
        Song(title="Freddie Freeloader", duration_seconds=584, track_number=2, album_id=kind_of_blue.id, play_count=60),
        Song(title="One More Time", duration_seconds=320, track_number=1, album_id=discovery.id, play_count=500),
        Song(title="Harder, Better, Faster, Stronger", duration_seconds=224, track_number=3, album_id=discovery.id, play_count=450),
        Song(title="Digital Love", duration_seconds=301, track_number=6, album_id=discovery.id, play_count=380),
    ]
    db.add_all(songs_data)
    db.flush()

    # ── Assign genres ──
    for s in songs_data[:3]:
        s.genres = [rock, pop]
        s.artists = [beatles]
    for s in songs_data[3:5]:
        s.genres = [jazz]
        s.artists = [miles]
    for s in songs_data[5:]:
        s.genres = [electronic, pop]
        s.artists = [daft]

    db.commit()
    print("✅ Seed data inserted successfully.")
    print(f"   Genres:  {db.query(Genre).count()}")
    print(f"   Artists: {db.query(Artist).count()}")
    print(f"   Albums:  {db.query(Album).count()}")
    print(f"   Songs:   {db.query(Song).count()}")

except Exception as e:
    db.rollback()
    print(f"❌ Error: {e}")
    raise
finally:
    db.close()
