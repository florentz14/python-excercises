"""Standard launcher for survey load demo."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "10_survey.py"), run_name="__main__")
