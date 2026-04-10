# -------------------------------------------------
# CRUD sencillo de estudiantes sobre Examples/data/students.csv
# Create / Read (list & detail) / Update / Delete. Guarda tras cada cambio.
# Buscar por SID (Student ID). Name sigue siendo único al crear.
# -------------------------------------------------

import csv
import subprocess
import sys
from datetime import date
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "students.csv"

FIELDNAMES = [
    "SID",
    "Name",
    "Age",
    "Major",
    "GPA",
    "City",
    "State",
    "EnrollmentYear",
    "CreditHoursCompleted",
    "Honors",
    "AttendanceRate",
    "ScholarshipUSD",
    "Status",
    "LastActivityDate",
]


def clear_screen() -> None:
    """Clear the terminal (Windows: cls, macOS/Linux: clear)."""
    if sys.platform == "win32":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)


def load_students() -> list[dict[str, str]]:
    if not CSV_PATH.is_file():
        return []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_students(rows: list[dict[str, str]]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def next_sid(rows: list[dict[str, str]]) -> str:
    """Siguiente SID numérico (10001, 10002, ...) a partir de los existentes."""
    highest = 10000
    for row in rows:
        sid = row.get("SID", "").strip()
        if sid.isdigit():
            highest = max(highest, int(sid))
    return str(highest + 1)


def find_index_by_name(rows: list[dict[str, str]], name: str) -> int:
    key = name.strip().casefold()
    for i, row in enumerate(rows):
        if row["Name"].strip().casefold() == key:
            return i
    return -1


def find_index_by_sid(rows: list[dict[str, str]], sid: str) -> int:
    key = sid.strip()
    if not key:
        return -1
    for i, row in enumerate(rows):
        if row.get("SID", "").strip() == key:
            return i
    return -1


def list_students(rows: list[dict[str, str]]) -> None:
    print("\n--- All students ---")
    if not rows:
        print("(none)")
        return
    for row in rows:
        print(
            f"  [{row['SID']}] {row['Name']}: age {row['Age']}, {row['Major']}, "
            f"GPA {row['GPA']}, {row['City']}, {row['State']}"
        )


def view_student(rows: list[dict[str, str]], sid: str) -> None:
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found (check SID).")
        return
    print("\n--- Detail ---")
    for k in FIELDNAMES:
        print(f"  {k}: {rows[i][k]}")


def create_student(rows: list[dict[str, str]]) -> None:
    print("\n--- Create student ---")
    name = input("Name (unique): ").strip()
    if not name:
        print("Name required.")
        return
    if find_index_by_name(rows, name) >= 0:
        print("That name already exists. Choose another or update the record.")
        return

    age = input("Age: ").strip()
    major = input("Major: ").strip()
    gpa = input("GPA: ").strip()
    city = input("City: ").strip()
    state = input("State (e.g. TX): ").strip()
    year = input("Enrollment year: ").strip()

    today = date.today().isoformat()
    row = {
        "SID": next_sid(rows),
        "Name": name,
        "Age": age,
        "Major": major,
        "GPA": gpa,
        "City": city,
        "State": state,
        "EnrollmentYear": year,
        "CreditHoursCompleted": "0",
        "Honors": "No",
        "AttendanceRate": "100.0",
        "ScholarshipUSD": "0",
        "Status": "Active",
        "LastActivityDate": today,
    }
    rows.append(row)
    save_students(rows)
    print(f"Created and saved (SID {row['SID']}).")


def update_student(rows: list[dict[str, str]]) -> None:
    print("\n--- Update student ---")
    sid = input("SID to update: ").strip()
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found (check SID).")
        return

    print("Leave blank to keep current value.\n")
    for field in FIELDNAMES:
        if field in ("Name", "SID"):
            continue
        current = rows[i][field]
        new = input(f"{field} [{current}]: ").strip()
        if new:
            rows[i][field] = new

    new_name = input(f"Name [{rows[i]['Name']}]: ").strip()
    if new_name and new_name != rows[i]["Name"]:
        j = find_index_by_name(rows, new_name)
        if j >= 0 and j != i:
            print("Another student already has that name. Name not changed.")
        else:
            rows[i]["Name"] = new_name

    save_students(rows)
    print("Updated and saved.")


def delete_student(rows: list[dict[str, str]]) -> None:
    print("\n--- Delete student ---")
    sid = input("SID to delete: ").strip()
    i = find_index_by_sid(rows, sid)
    if i < 0:
        print("Student not found (check SID).")
        return
    confirm = input(
        f"Delete SID {rows[i]['SID']} ({rows[i]['Name']})? Type yes: "
    ).strip().casefold()
    if confirm != "yes":
        print("Cancelled.")
        return
    del rows[i]
    save_students(rows)
    print("Deleted and saved.")


def menu() -> str:
    print("\n=== Student CRUD ===")
    print("1) List students")
    print("2) View student by SID")
    print("3) Create student")
    print("4) Update student")
    print("5) Delete student")
    print("6) Exit")
    return input("Option: ").strip()


def main() -> None:
    rows = load_students()
    while True:
        clear_screen()
        choice = menu()
        if choice == "6":
            print("Bye.")
            break
        if choice == "1":
            list_students(rows)
        elif choice == "2":
            view_student(rows, input("SID: ").strip())
        elif choice == "3":
            create_student(rows)
        elif choice == "4":
            update_student(rows)
        elif choice == "5":
            delete_student(rows)
        else:
            print("Invalid option.")
        input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
