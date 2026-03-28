# -------------------------------------------------
# File Name: 30_csv_full_operations.py
# Created: 2026-03-27
# Description: CSV Full Operations Practice (writer, DictReader/DictWriter, update, delete)
# -------------------------------------------------

import csv
from pathlib import Path

FILE_NAME = Path(__file__).resolve().parent / "students.csv"


# -------------------------------------------------
# 1) Creating CSV file
# -------------------------------------------------
def create_csv() -> None:
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Major", "GPA"])
    print("CSV file created.\n")


# -------------------------------------------------
# 2) Adding one row
# -------------------------------------------------
def add_row() -> None:
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Alice", 20, "Computer Sci", 3.8])
    print("One row added.\n")


# -------------------------------------------------
# 3) Adding multiple rows
# -------------------------------------------------
def add_multiple_rows() -> None:
    rows = [
        ["Bob", 22, "Math", 3.2],
        ["Charlie", 19, "Physics", 3.6],
        ["Diana", 21, "Biology", 3.9],
    ]

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Multiple rows added.\n")


# -------------------------------------------------
# 4) Reading rows
# -------------------------------------------------
def read_rows() -> None:
    print("Reading CSV:")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


# -------------------------------------------------
# 5) 2nd Approach
# -------------------------------------------------
def read_with_dict() -> None:
    print("Reading with DictReader:")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    print()


def write_with_dict() -> None:
    print("Writing with DictWriter:")
    data = [
        {"Name": "Ethan", "Age": 23, "Major": "Computer Sci", "GPA": 3.4},
    ]

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "Age", "Major", "GPA"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # DictWriter has writerow, not writerows — loop each dict
        for row in data:
            writer.writerow(row)
    print("Row added using DictWriter.\n")


# -------------------------------------------------
# 6) Append new rows
# -------------------------------------------------
def append_rows() -> None:
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Frank", 24, "Engineering", 3.1])
    print("Row appended.\n")


# -------------------------------------------------
# 7) Updating (row, column, cell)
# -------------------------------------------------
def update_row() -> None:
    rows: list[list[str]] = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Update example: change Bob's GPA
    for row in rows:
        if row and row[0] == "Bob":
            row[3] = "3.7"

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Row updated.\n")


# -------------------------------------------------
# 8) Deleting (row)
# -------------------------------------------------
def delete_row() -> None:
    rows: list[list[str]] = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Remove Charlie (keep header and skip empty lines)
    rows = [row for row in rows if row and row[0] != "Charlie"]

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Row deleted.\n")


# -------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------
def main() -> None:
    create_csv()
    add_row()
    add_multiple_rows()
    read_rows()

    read_with_dict()
    write_with_dict()

    append_rows()
    read_rows()

    update_row()
    read_rows()

    delete_row()
    read_rows()


if __name__ == "__main__":
    main()
