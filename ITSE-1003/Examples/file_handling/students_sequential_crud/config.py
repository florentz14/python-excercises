"""Rutas y columnas del CSV de demo (secuencial -> modular CRUD)."""

from pathlib import Path

# Examples/data/students_sequential_demo.csv
_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
CSV_PATH = _DATA_DIR / "students_sequential_demo.csv"

FIELDNAMES = ["SID", "Name", "Age", "Major"]
