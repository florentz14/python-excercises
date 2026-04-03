# -------------------------------------------------
# File Name: 34_csv_dictreader_basic.py
# Created: 2026-04-02
# Description: Minimal read with DictReader and print each row as a dict.
#              IDLE-style idea; UTF-8, newline="", dedicated demo CSV name.
#              For filtering rows, see 36_csv_dictreader_filter_by_major.py.
# -------------------------------------------------

import csv
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "students_dictreader_demo.csv"

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
