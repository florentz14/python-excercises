from __future__ import annotations

from books_app.app.schemas.backend import BackendName
from books_app.app.services.books_service import run_backend_demo


def run_cli(backend: BackendName | None = None):
    if backend:
        run_backend_demo(backend)
        return

    print("=" * 64)
    print("BOOKS APP - SELECT BACKEND")
    print("=" * 64)
    print("1 - SQLite")
    print("2 - PostgreSQL")
    print("3 - SQLAlchemy (SQLite)")
    print("4 - MongoDB")
    print("5 - Classic books.db example")
    print("6 - Exit")
    print("=" * 64)

    choice = input("Choose backend (1-6): ").strip()
    mapping: dict[str, BackendName] = {
        "1": "sqlite",
        "2": "postgres",
        "3": "sqlalchemy",
        "4": "mongo",
        "5": "example",
    }
    if choice == "6":
        print("Goodbye!")
        return
    selected = mapping.get(choice)
    if not selected:
        print("Invalid choice.")
        return
    run_backend_demo(selected)
