# -------------------------------------------------
# Descripción: Extiende v2: cuenta por carrera (Major) y resume edades —
# edad mínima/máxima, promedio, y nombres del/de los más jóvenes y más viejos
# (si hay empate en edad, se listan todos).
# -------------------------------------------------

from pathlib import Path

import csv

_STUDENTS_CSV = Path(__file__).resolve().parent.parent / "data" / "students.csv"

major_count = {}

with open(_STUDENTS_CSV, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    major = row["Major"]
    major_count[major] = major_count.get(major, 0) + 1

print("Students per major:")
for major in major_count:
    print(f"  {major}: {major_count[major]}")

if not rows:
    print("\n(No hay filas de estudiantes en el CSV.)")
else:
    ages = [int(row["Age"]) for row in rows]
    total = sum(ages)
    count = len(ages)
    avg_age = total / count
    min_age = min(ages)
    max_age = max(ages)

    youngest_names = [row["Name"] for row in rows if int(row["Age"]) == min_age]
    oldest_names = [row["Name"] for row in rows if int(row["Age"]) == max_age]

    print("\nAge summary:")
    print(f"  Youngest age: {min_age} - {', '.join(youngest_names)}")
    print(f"  Oldest age:   {max_age} - {', '.join(oldest_names)}")
    print(f"  Average age:  {avg_age:.2f}")
