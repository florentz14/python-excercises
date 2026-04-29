"""Standard launcher for books mongo demo."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "07_books_mongo.py"), run_name="__main__")
