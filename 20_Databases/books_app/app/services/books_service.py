from __future__ import annotations

import runpy
from pathlib import Path

from books_app.app.schemas.backend import BackendName

SCRIPT_MAP: dict[BackendName, str] = {
    "sqlite": "legacy/04_books_sqlite.py",
    "postgres": "legacy/05_books_postgres.py",
    "sqlalchemy": "legacy/06_books_sqlalchemy.py",
    "mongo": "legacy/07_books_mongo.py",
    "example": "legacy/books_example.py",
}


def run_backend_demo(backend: BackendName):
    script_name = SCRIPT_MAP[backend]
    project_dir = Path(__file__).resolve().parents[2]
    script_path = project_dir / script_name
    runpy.run_path(str(script_path), run_name="__main__")
