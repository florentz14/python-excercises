"""Standard launcher for ATM app."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "02_atm_mysql_app.py"), run_name="__main__")
