# -------------------------------------------------
# File Name: 31_csv_interactive_menu.py
# Created: 2026-03-28
# Description: Interactive CSV student CRUD with input() and validations (extends 30_csv_full_operations).
# -------------------------------------------------

from __future__ import annotations

import csv
from pathlib import Path

FILE_NAME = Path(__file__).resolve().parent / "students.csv"
FIELDNAMES = ["Name", "Age", "Major", "GPA"]

# --- validation limits ---
MIN_NAME_LEN = 2
MAX_NAME_LEN = 50
MIN_AGE = 16
MAX_AGE = 99
MIN_MAJOR_LEN = 2
MAX_MAJOR_LEN = 80
GPA_MIN = 0.0
GPA_MAX = 4.0


def _strip_or_empty(s: str) -> str:
    return s.strip()


def input_valid_name(prompt: str = "Name: ") -> str:
    """Name 2–50 chars; letters (incl. accents), spaces, hyphens, apostrophes."""
    while True:
        raw = input(prompt).strip()
        if len(raw) < MIN_NAME_LEN or len(raw) > MAX_NAME_LEN:
            print(f"  Name must be {MIN_NAME_LEN}-{MAX_NAME_LEN} characters.\n")
            continue
        if not all(ch.isalpha() or ch in " -'" for ch in raw):
            print("  Use only letters, spaces, hyphens, and apostrophes.\n")
            continue
        return raw


def input_valid_age(prompt: str = "Age: ") -> int:
    while True:
        raw = input(prompt).strip()
        try:
            age = int(raw)
        except ValueError:
            print("  Enter a whole number.\n")
            continue
        if age < MIN_AGE or age > MAX_AGE:
            print(f"  Age must be between {MIN_AGE} and {MAX_AGE}.\n")
            continue
        return age


def input_valid_major(prompt: str = "Major: ") -> str:
    while True:
        raw = input(prompt).strip()
        if len(raw) < MIN_MAJOR_LEN or len(raw) > MAX_MAJOR_LEN:
            print(f"  Major must be {MIN_MAJOR_LEN}-{MAX_MAJOR_LEN} characters.\n")
            continue
        return raw


def input_valid_gpa(prompt: str = "GPA (0.0–4.0): ") -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            gpa = float(raw)
        except ValueError:
            print("  Enter a decimal number (e.g. 3.5).\n")
            continue
        if gpa < GPA_MIN or gpa > GPA_MAX:
            print(f"  GPA must be between {GPA_MIN} and {GPA_MAX}.\n")
            continue
        return round(gpa, 2)


def input_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes", "s", "si", "sí"):
            return True
        if ans in ("n", "no"):
            return False
        print("  Answer y or n.\n")


def load_rows() -> list[list[str]]:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return list(csv.reader(file))


def save_rows(rows: list[list[str]]) -> None:
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(rows)


def student_names_lower(rows: list[list[str]]) -> set[str]:
    if not rows:
        return set()
    return {row[0].strip().lower() for row in rows[1:] if row and row[0].strip()}


def create_csv_interactive() -> None:
    if FILE_NAME.exists() and not input_yes_no("students.csv exists. Overwrite? (y/n): "):
        print("Cancelled.\n")
        return
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(FIELDNAMES)
    print("CSV created with header only.\n")


def add_student_interactive() -> None:
    rows = load_rows()
    existing = student_names_lower(rows)
    print("--- New student ---")
    name = input_valid_name()
    if name.lower() in existing:
        print(f"  A student named '{name}' already exists.\n")
        return
    age = input_valid_age()
    major = input_valid_major()
    gpa = input_valid_gpa()
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([name, age, major, gpa])
    print(f"Added: {name}\n")


def add_multiple_interactive() -> None:
    while True:
        raw = input("How many students to add? ").strip()
        try:
            n = int(raw)
        except ValueError:
            print("  Enter a positive integer.\n")
            continue
        if n < 1 or n > 50:
            print("  Use a number between 1 and 50.\n")
            continue
        break
    rows = load_rows()
    existing = student_names_lower(rows)
    added = 0
    for i in range(1, n + 1):
        print(f"\n--- Student {i} of {n} ---")
        name = input_valid_name()
        if name.lower() in existing:
            print(f"  Skipped: '{name}' already exists.\n")
            continue
        age = input_valid_age()
        major = input_valid_major()
        gpa = input_valid_gpa()
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([name, age, major, gpa])
        existing.add(name.lower())
        added += 1
        print(f"Added: {name}")
    print(f"\nFinished. {added} row(s) added.\n")


def read_rows_plain() -> None:
    print("--- csv.reader ---")
    for row in load_rows():
        print(row)
    print()


def read_rows_dict() -> None:
    print("--- DictReader ---")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            print(dict(row))
    print()


def add_student_dictwriter() -> None:
    """Same data as add_student but uses DictWriter (demo of API)."""
    rows = load_rows()
    existing = student_names_lower(rows)
    print("--- New student (DictWriter) ---")
    name = input_valid_name()
    if name.lower() in existing:
        print(f"  A student named '{name}' already exists.\n")
        return
    age = input_valid_age()
    major = input_valid_major()
    gpa = input_valid_gpa()
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        w = csv.DictWriter(file, fieldnames=FIELDNAMES)
        w.writerow(
            {"Name": name, "Age": age, "Major": major, "GPA": gpa}
        )
    print(f"Added with DictWriter: {name}\n")


def update_student_interactive() -> None:
    rows = load_rows()
    if len(rows) < 2:
        print("No student rows to update.\n")
        return
    target = input("Student name to update (exact match): ").strip()
    if not target:
        print("Empty name.\n")
        return
    idx = None
    for i, row in enumerate(rows):
        if i == 0:
            continue
        if row and row[0].strip() == target:
            idx = i
            break
    if idx is None:
        print(f"No student named '{target}'.\n")
        return
    print("Field to update: 1=Age  2=Major  3=GPA")
    choice = input("Choice (1-3): ").strip()
    row = rows[idx]
    if choice == "1":
        row[1] = str(input_valid_age("New age: "))
    elif choice == "2":
        row[2] = input_valid_major("New major: ")
    elif choice == "3":
        row[3] = str(input_valid_gpa("New GPA: "))
    else:
        print("Invalid field.\n")
        return
    save_rows(rows)
    print("Updated.\n")


def delete_student_interactive() -> None:
    rows = load_rows()
    if len(rows) < 2:
        print("No student rows to delete.\n")
        return
    target = input("Student name to delete (exact match): ").strip()
    if not target:
        print("Empty name.\n")
        return
    new_rows = [rows[0]]
    removed = False
    for row in rows[1:]:
        if row and row[0].strip() == target:
            removed = True
            continue
        new_rows.append(row)
    if not removed:
        print(f"No student named '{target}'.\n")
        return
    if not input_yes_no(f"Delete '{target}' permanently? (y/n): "):
        print("Cancelled.\n")
        return
    save_rows(new_rows)
    print("Deleted.\n")


def csv_ready() -> bool:
    if not FILE_NAME.exists():
        print("students.csv not found. Use option 1 first.\n")
        return False
    return True


def main() -> None:
    while True:
        print("=" * 52)
        print(" Interactive CSV — students.csv (validated input)")
        print("=" * 52)
        print(" 1) Create CSV (header only)")
        print(" 2) Add one student (csv.writer + validation)")
        print(" 3) Add multiple students")
        print(" 4) Read all rows (csv.reader)")
        print(" 5) Read all rows (DictReader)")
        print(" 6) Add one student (DictWriter + validation)")
        print(" 7) Update a student (by name)")
        print(" 8) Delete a student (by name)")
        print(" 0) Exit")
        print("=" * 52)

        choice = input("Choice: ").strip()
        if choice == "0":
            print("Goodbye.\n")
            break
        if choice == "1":
            create_csv_interactive()
        elif choice == "2":
            if csv_ready():
                add_student_interactive()
        elif choice == "3":
            if csv_ready():
                add_multiple_interactive()
        elif choice == "4":
            if csv_ready():
                read_rows_plain()
        elif choice == "5":
            if csv_ready():
                read_rows_dict()
        elif choice == "6":
            if csv_ready():
                add_student_dictwriter()
        elif choice == "7":
            if csv_ready():
                update_student_interactive()
        elif choice == "8":
            if csv_ready():
                delete_student_interactive()
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
