# -------------------------------------------------
# Descripción: Lee un CSV de estudiantes y cuenta cuántos hay por carrera (Major).
# Cada fila que entrega csv.DictReader es un diccionario con las claves del encabezado,
# por ejemplo: {"Name": "Alice", "Age": "20", "Major": "Computer Sci", "GPA": "3.8"}.
# Se usa un diccionario major_count para acumular: clave = nombre de la carrera,
# valor = número de estudiantes en esa carrera.
# -------------------------------------------------

from pathlib import Path

import csv

_STUDENTS_CSV = Path(__file__).resolve().parent.parent / "data" / "students.csv"

major_count = {}  # create a new dictionary

with open(_STUDENTS_CSV, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    reder_list = list(reader) # convert the reader to a list

    for row in reder_list:  # {'Name': 'Alice', 'Age': '20', 'Major': 'Computer Sci', ...}
        major = row["Major"]  # Get the major, now major = "Computer Sci"
        # or "Math", "Physics", etc.
        major_count[major] = major_count.get(major, 0) + 1
        

print("Students per major:")
for major in major_count:
    print(f"{major}: {major_count[major]}")
