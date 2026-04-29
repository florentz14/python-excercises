"""Backward-compatible launcher for books_app (example backend)."""

from books_app.app.main import run


if __name__ == "__main__":
    import sys

    sys.argv = [sys.argv[0], "example"]
    run()
