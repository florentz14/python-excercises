# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_update_sequential_v1.py
# Author: Florentino
# Date: 4/10/2026
# Description: Sequential CSV update/delete on students_sequential_demo.csv; see students_sequential_crud for menu.
# -------------------------------------------------

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "students_sequential_demo.csv"
FIELDNAMES = ["SID", "Name", "Age", "Major"]

# we cannot get a row and modify that row and that's it
# CSV UPDATE -> READ, MODIFY, REWRITE
rows = []  # TEMPORARILY HOLDS THE CSV FILE as a list of dicts
# 2 step process read and then hold, and then overwrite the csv file

# STEP 1 - READ
with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # CSV: 50001 = Alice (20, Computer Sci); 50003 = Alice (21, Physics) - mismo nombre, distinto SID.
        if row["SID"] == "50001":
            row["Major"] = "Data Science"  # solo esta fila

        rows.append(row)

# STEP 2 - WRITE (overwrite file)
with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)

print("CSV updated")

# Si usas row["Name"] == "Alice", se actualizan 50001 y 50003. Con SID eliges una sola fila.

# STEP 3 - READ (delete: append all rows except the one you want to remove)
rows = []
with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["SID"] != "50002":  # append all but this SID (Bob en el demo)
            rows.append(row)

# STEP 4 - WRITE (overwrite file)
with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)

print("CSV updated (delete)")

# Variante por nombre (borra todos los que se llamen igual): if row["Name"] != "Bob":
# No uses rows.remove(row) mientras lees con DictReader; arma una lista nueva con append.
