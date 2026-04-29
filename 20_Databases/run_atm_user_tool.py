"""Standard launcher for ATM user tool."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "03_atm_user_tool.py"), run_name="__main__")
