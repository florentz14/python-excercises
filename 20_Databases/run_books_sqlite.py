"""Standard launcher for books sqlite demo."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "04_books_sqlite.py"), run_name="__main__")
