"""Backward-compatible launcher for books_app (postgres backend)."""

from books_app.app.main import run


if __name__ == "__main__":
    import sys

    sys.argv = [sys.argv[0], "postgres"]
    run()
