"""Standard launcher for survey 2002 filter demo."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "11_survey.py"), run_name="__main__")
