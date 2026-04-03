# -------------------------------------------------
# File Name: 36_csv_dictreader_filter_by_major.py
# Created: 2026-04-02
# Description: DictReader: filter names where Major is "Computer Sci", then
#              count how many students per major.
# -------------------------------------------------

import csv
from pathlib import Path

# create a file path for the csv file
csv_path = Path(__file__).resolve().parent / "students_dictreader_demo.csv"

# read the csv file and store the rows in a list
with open(csv_path, "r", newline="", encoding="utf-8") as file:
    # read the csv file and store the rows in a list
    rows = list(csv.DictReader(file))

print("Names (Major == Computer Sci):")
for row in rows:
    if row["Major"] == "Computer Sci":
        print(row["Name"])

# create a dictionary to store the count of students per major
major_count: dict[str, int] = {}

# loop through the rows and count the number of students per major
for row in rows:
    # get the major of the student
    major: str = row["Major"]
    # increment the count of the major
    major_count[major] = major_count.get(major, 0) + 1

print("\nCount by major:")
# loop through the major_count dictionary and print the major and the count
for major in sorted(major_count):
    print(f"  {major}: {major_count[major]}")
