# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_sequential_crud/delete_student.py
# Author: Florentino
# Date: 4/10/2026
# Description: Delete one student by SID after confirmation; rewrite CSV.
# -------------------------------------------------

from storage import load_students, save_students, find_index_by_sid


def run_delete():
    print("\n--- Delete student ---")
    rows = load_students()
    sid = input("SID to delete: ").strip()
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found.")
        return
    confirm = input(
        f"Delete SID {rows[i]['SID']} ({rows[i]['Name']})? Type yes: "
    ).strip().casefold()
    if confirm != "yes":
        print("Cancelled.")
        return
    rows = [row for row in rows if row["SID"].strip() != sid.strip()]
    save_students(rows)
    print("Deleted and saved.")
