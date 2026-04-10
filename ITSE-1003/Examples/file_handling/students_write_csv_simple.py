# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_write_csv_simple.py
# Author: Florentino
# Date: 4/10/2026
# Description: Minimal CSV create/read/update/delete demo with DictReader and DictWriter.
# -------------------------------------------------

import csv
from pathlib import Path

OUT_CSV = Path(__file__).resolve().parent.parent / "data" / "students-new.csv"
FIELDNAMES = ["SID", "Name", "Age", "Major"]


def load_students():
    """READ: devuelve una lista de filas (dict por estudiante)."""
    with open(OUT_CSV, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(rows):
    """Escribe todas las filas al CSV (CREATE inicial o tras UPDATE/DELETE)."""
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


# ----- CREATE: archivo desde una lista en memoria -----
students = [
    {"SID": "10001", "Name": "Alice", "Age": 20, "Major": "Computer Sci"},
    {"SID": "10002", "Name": "Bob", "Age": 22, "Major": "Math"},
    {"SID": "10003", "Name": "Charlie", "Age": 19, "Major": "Physics"},
]
save_students(students)
print(f"CREATE - wrote {OUT_CSV}\n")

# ----- READ -----
for row in load_students():
    print(row)

# ----- UPDATE: cargar, modificar por SID, guardar -----
rows = load_students()
for row in rows:
    if row["SID"] == "10002":  # Bob
        row["Age"] = "23"
        row["Major"] = "Statistics"
        break
save_students(rows)
print("\nUPDATE - SID 10002 (Bob) -> age 23, major Statistics:")
for row in load_students():
    print(row)

# ----- DELETE: cargar, quitar fila por SID, guardar -----
rows = load_students()
rows = [row for row in rows if row["SID"] != "10003"]  # Charlie
save_students(rows)
print("\nDELETE - removed SID 10003 (Charlie):")
for row in load_students():
    print(row)
