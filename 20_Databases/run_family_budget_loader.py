"""Standard launcher for family budget loader."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "08_family_budget_loader.py"), run_name="__main__")
