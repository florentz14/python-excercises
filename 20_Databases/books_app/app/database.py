from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

SQLITE_DB_FILE = DATA_DIR / "books_catalog.db"
SQLALCHEMY_DB_FILE = DATA_DIR / "books_sqlalchemy.db"

POSTGRES_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "books_db"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
}

MONGO_CONFIG = {
    "uri": os.getenv("MONGO_URI", "mongodb://localhost:27017"),
    "db": os.getenv("MONGO_DB", "books_db"),
}
