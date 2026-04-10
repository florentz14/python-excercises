# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_sequential_crud/config.py
# Author: Florentino
# Date: 4/10/2026
# Description: CSV path and column names for the sequential demo dataset.
# -------------------------------------------------

from pathlib import Path

# Examples/data/students_sequential_demo.csv
_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
CSV_PATH = _DATA_DIR / "students_sequential_demo.csv"

FIELDNAMES = ["SID", "Name", "Age", "Major"]
