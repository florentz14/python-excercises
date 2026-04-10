# -------------------------------------------------
# Descripción: Lee un CSV de estudiantes y imprime los nombres de los estudiantes con edad mayor a 21.
# Ejemplo mínimo: imprimir nombres de estudiantes con edad > 21.
# Cada fila que entrega csv.DictReader es un diccionario con las claves del encabezado,
# por ejemplo: {"Name": "Alice", "Age": "20", "Major": "Computer Sci", "GPA": "3.8"}.
# -------------------------------------------------

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "students.csv"

with open(CSV_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Students older than 21:")

    for row in reader:
        age = int(row["Age"])

        if age > 21:
            print(row["Name"])
