# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_sequential_crud/read_students.py
# Author: Florentino
# Date: 4/10/2026
# Description: List all students and print one record by SID (read operations).
# -------------------------------------------------

from config import FIELDNAMES
from storage import load_students, find_index_by_sid


def list_all():
    rows = load_students()
    print("\n--- All students ---")
    if not rows:
        print("(none)")
        return
    for row in rows:
        print(
            f"  [{row['SID']}] {row['Name']}: age {row['Age']}, {row['Major']}"
        )


def view_by_sid():
    sid = input("SID: ").strip()
    rows = load_students()
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found.")
        return
    print("\n--- Detail ---")
    for k in FIELDNAMES:
        print(f"  {k}: {rows[i][k]}")
