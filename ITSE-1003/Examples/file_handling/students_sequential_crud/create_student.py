# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_sequential_crud/create_student.py
# Author: Florentino
# Date: 4/10/2026
# Description: Create a student row with an auto-generated SID and save to CSV.
# -------------------------------------------------

from storage import load_students, save_students, next_sid


def _name_exists(rows, name):
    key = name.strip().casefold()
    for row in rows:
        if row["Name"].strip().casefold() == key:
            return True
    return False


def run_create():
    print("\n--- Create student ---")
    rows = load_students()
    name = input("Name (unique in this demo): ").strip()
    if not name:
        print("Name required.")
        return
    if _name_exists(rows, name):
        print("That name already exists.")
        return

    age = input("Age: ").strip()
    major = input("Major: ").strip()

    row = {
        "SID": next_sid(rows),
        "Name": name,
        "Age": age,
        "Major": major,
    }
    rows.append(row)
    save_students(rows)
    print(f"Saved (SID {row['SID']}).")
