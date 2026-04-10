# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_oldest_simple.py
# Author: Florentino
# Date: 4/10/2026
# Description: One-pass CSV scan for oldest/youngest ages and names (handles ties).
# -------------------------------------------------

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "students.csv"

oldest_age = None
oldest_names = []

youngest_age = None
youngest_names = []

with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        age = int(row["Age"])
        name = row["Name"]

        if oldest_age is None or age > oldest_age:
            oldest_age = age
            oldest_names = [name]
        elif age == oldest_age:
            oldest_names.append(name)

        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_names = [name]
        elif age == youngest_age:
            youngest_names.append(name)

if oldest_age is None:
    print("No students in file.")
else:
    print(f"The oldest student(s): {', '.join(oldest_names)} (age {oldest_age})")
    print(f"The youngest student(s): {', '.join(youngest_names)} (age {youngest_age})")
