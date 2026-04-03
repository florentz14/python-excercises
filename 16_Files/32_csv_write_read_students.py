# -------------------------------------------------
# File Name: 32_csv_write_read_students.py
# Created: 2026-04-02
# Description: Write a small students CSV then read it back. Improved IDLE-style
#              example: utf-8, newline="" for csv, DictReader (no fragile indices).
# -------------------------------------------------

import csv

from file_paths import GEN_DIR

CSV_PATH = GEN_DIR / "students.csv"

# Write CSV
with CSV_PATH.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Major"])
    writer.writerow(["Alice", 20, "Computer Sci"])
    writer.writerow(["Bob", 22, "Math"])
    writer.writerow(["Charlie", 19, "Physics"])
    writer.writerow(["Diana", 21, "Biology"])

# Read CSV (DictReader skips using row[0], row[1], … if columns move)
with CSV_PATH.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(
            f"Name: {row['Name']}, Age: {row['Age']}, Major: {row['Major']}"
        )
