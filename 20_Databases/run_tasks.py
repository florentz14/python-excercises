"""Standard launcher for tasks demo."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "09_tasks.py"), run_name="__main__")
