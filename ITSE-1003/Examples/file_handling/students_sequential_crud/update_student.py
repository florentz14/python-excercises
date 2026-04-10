"""UPDATE: leer todo, cambiar una fila por SID, reescribir."""

from config import FIELDNAMES
from storage import load_students, save_students, find_index_by_sid


def _name_exists_other(rows, name, skip_index):
    key = name.strip().casefold()
    for i, row in enumerate(rows):
        if i == skip_index:
            continue
        if row["Name"].strip().casefold() == key:
            return True
    return False



def run_update():
    print("\n--- Update student ---")
    rows = load_students()
    sid = input("SID to update: ").strip()
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found.")
        return

    print("Leave blank to keep current value.\n")
    for field in FIELDNAMES:
        if field in ("SID", "Name"):
            continue
        current = rows[i][field]
        new = input(f"{field} [{current}]: ").strip()
        if new:
            rows[i][field] = new

    new_name = input(f"Name [{rows[i]['Name']}]: ").strip()
    if new_name and new_name != rows[i]["Name"]:
        if _name_exists_other(rows, new_name, i):
            print("Another student has that name. Name not changed.")
        else:
            rows[i]["Name"] = new_name

    save_students(rows)
    print("Updated and saved.")
