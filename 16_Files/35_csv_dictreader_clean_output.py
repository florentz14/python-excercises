# -------------------------------------------------
# File Name: 35_csv_dictreader_clean_output.py
# Created: 2026-04-02
# Description: DictReader — each row is a dict; print one line per student, then
#              total age (sum) and average age.
# -------------------------------------------------

import csv
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "students_dictreader_demo.csv"

total_age: float = 0
count: int = 0

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name: str = row["Name"]
        age: int = int(row["Age"])
        major: str = row["Major"]

        print(f"{name} is {age} years old and studies {major}")

        total_age += age
        count += 1

if count:
    average_age: float = total_age / count
    print(f"\nTotal age (sum): {total_age}")
    print(f"Average age: {average_age:.1f}")    
else:
    print("\nNo student rows to summarize.")
