from __future__ import annotations

import sys

from books_app.app.routers.menu import run_cli
from books_app.app.schemas.backend import BackendName


def run():
    backend: BackendName | None = None
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()
        if arg in {"sqlite", "postgres", "sqlalchemy", "mongo", "example"}:
            backend = arg  # type: ignore[assignment]
    run_cli(backend)


if __name__ == "__main__":
    run()
