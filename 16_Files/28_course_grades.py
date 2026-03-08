# -------------------------------------------------
# File Name: 28_course_grades.py
# Description: Load grades, compute final grade, list approved/suspended
# -------------------------------------------------

import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "grades.csv"


def load_grades(filepath: str | Path) -> list[dict]:
    """Load grades CSV. Returns list of dicts sorted by surname."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Theory1"] = float(row["Theory1"])
            row["Theory2"] = float(row["Theory2"])
            row["Practice"] = float(row["Practice"])
            row["Attendance"] = float(row["Attendance"].replace("%", "").strip())
            rows.append(row)
    rows.sort(key=lambda x: x["Surname"])
    return rows


def add_final_grade(students: list[dict]) -> list[dict]:
    """Add 'final_grade' to each dict. 30% T1 + 30% T2 + 40% Practice."""
    for s in students:
        nf = 0.30 * s["Theory1"] + 0.30 * s["Theory2"] + 0.40 * s["Practice"]
        s["final_grade"] = round(nf, 2)
    return students


def approved_suspended(students: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (approved, suspended). Pass: attendance>=75%, exams>=4, final>=5."""
    approved = []
    suspended = []
    for s in students:
        att_ok = s["Attendance"] >= 75
        ex_ok = s["Theory1"] >= 4 and s["Theory2"] >= 4 and s["Practice"] >= 4
        nf_ok = s["final_grade"] >= 5
        if att_ok and ex_ok and nf_ok:
            approved.append(s)
        else:
            suspended.append(s)
    return approved, suspended


if __name__ == "__main__":
    students = load_grades(DATA)
    students = add_final_grade(students)
    approved, suspended = approved_suspended(students)

    print("--- APPROVED ---")
    for s in approved:
        print(f"  {s['Surname']} {s['Name']}: {s['final_grade']}")

    print("\n--- SUSPENDED ---")
    for s in suspended:
        print(f"  {s['Surname']} {s['Name']}: {s['final_grade']}")
