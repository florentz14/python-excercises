# -------------------------------------------------
# File Name: ITSE-1003/Lab2CSV/lab2_csv_manipulation.py
# Author: Florentino Baez
# Course: ITSE-1003 (Python for Data Science)
# Professor: Mauricio Quiroga
# Date: 3/27/2026
# Description: Lab 2 - CSV manipulation with csv.DictReader, summaries, filters, stretch output.
# -------------------------------------------------

import csv
from pathlib import Path

# Paths next to this script (works regardless of current working directory)
_LAB_DIR = Path(__file__).resolve().parent
CSV_PATH = _LAB_DIR / "lab2_students.csv"
SUMMARY_PATH = _LAB_DIR / "lab2_summary.txt"


# -------------------------------------------------
# Task 1 - Import and open the file
# -------------------------------------------------
with CSV_PATH.open(mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    # Load all rows once so later tasks can scan the list without re-opening the file
    students = list(reader)


# -------------------------------------------------
# Task 2 - Print all students in a clean format
# -------------------------------------------------
print("\n--- Task 2: All Students ---")
for student in students:
    print(
        f"Name: {student['Name']} | "
        f"Age: {student['Age']} | "
        f"Major: {student['Major']} | "
        f"GPA: {student['GPA']}"
    )


# -------------------------------------------------
# Task 3 - Calculate the average age
# -------------------------------------------------
total_age = sum(int(s["Age"]) for s in students)
average_age = total_age / len(students)
print(f"\nAverage age: {average_age:.1f}")


# -------------------------------------------------
# Task 4 - Find the oldest student
# -------------------------------------------------
oldest_student = max(students, key=lambda s: int(s["Age"]))
print(
    f"\nOldest student: {oldest_student['Name']} "
    f"({oldest_student['Age']} years old)"
)


# -------------------------------------------------
# Task 5 - Print only Computer Sci students
# -------------------------------------------------
print("\n--- Computer Sci Students ---")
for student in students:
    if student["Major"] == "Computer Sci":
        print(student["Name"])


# -------------------------------------------------
# Task 6 - Count how many students are in each major
# -------------------------------------------------
major_count: dict[str, int] = {}
for student in students:
    major = student["Major"]
    major_count[major] = major_count.get(major, 0) + 1

print("\n--- Students per Major ---")
for major, count in major_count.items():
    print(f"{major}: {count}")


# -------------------------------------------------
# Task 7 - Print students with GPA 3.5 or higher
# -------------------------------------------------
print("\n--- Students with GPA >= 3.5 ---")
for student in students:
    if float(student["GPA"]) >= 3.5:
        print(student["Name"])


# -------------------------------------------------
# Stretch challenge (optional)
# -------------------------------------------------
total_gpa = sum(float(s["GPA"]) for s in students)
average_gpa = total_gpa / len(students)
print(f"\nAverage GPA: {average_gpa:.2f}")

print("\n--- Students older than 21 ---")
for student in students:
    if int(student["Age"]) > 21:
        print(student["Name"])

with SUMMARY_PATH.open(mode="w", encoding="utf-8") as summary_file:
    summary_file.write("Lab 2 Summary\n")
    summary_file.write("-----------------\n")
    summary_file.write(f"Average Age: {average_age:.1f}\n")
    summary_file.write(f"Average GPA: {average_gpa:.2f}\n")
    summary_file.write("Students older than 21:\n")
    for student in students:
        if int(student["Age"]) > 21:
            summary_file.write(f"- {student['Name']}\n")

print(f"\nSummary written to {SUMMARY_PATH.name}")
