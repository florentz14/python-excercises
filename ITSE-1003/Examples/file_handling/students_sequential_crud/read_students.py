"""Listar y ver detalle por SID."""

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
