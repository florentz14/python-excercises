# -------------------------------------------------
# File Name: 33_csv_write_read_students_reader.py
# Created: 2026-04-02
# Description: Same flow as a typical IDLE week-2 example: csv.writer then
#              csv.reader with row[0], row[1], row[2]. UTF-8 and newline=""
#              fix common issues; uses its own CSV name so it does not clobber
#              students.csv from other demos in this folder.
# -------------------------------------------------

import csv
from pathlib import Path

# Dedicated filename for this demo (does not overwrite students.csv from 30_/31_).
students_csv = Path(__file__).resolve().parent / "students_reader_demo.csv"

# Write CSV
with open(students_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Major"])
    writer.writerow(["Alice", 20, "Computer Sci"])
    writer.writerow(["Bob", 22, "Math"])
    writer.writerow(["Charlie", 19, "Physics"])
    writer.writerow(["Diana", 21, "Biology"])

# Read CSV
with open(students_csv, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        print(f"Name: {row[0]}, Age: {row[1]}, Major: {row[2]}")
