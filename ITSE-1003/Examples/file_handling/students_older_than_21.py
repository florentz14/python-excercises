# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_older_than_21.py
# Author: Florentino
# Date: 4/10/2026
# Description: Print names of students with age greater than 21 (DictReader minimal example).
# -------------------------------------------------

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "students.csv"

with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Students older than 21:")

    for row in reader:
        age = int(row["Age"])

        if age > 21:
            print(row["Name"])
