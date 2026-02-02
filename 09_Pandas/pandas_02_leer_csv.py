"""
Pandas - Ejemplo 2: Leer un CSV (archivo tipo Excel)
====================================================
Tema: Pandas (09_Pandas)
Descripción: pd.read_csv() para cargar un archivo .csv en un DataFrame.
"""

import pandas as pd

# Crear un CSV de ejemplo en memoria (en la práctica sería un archivo)
from io import StringIO

csv_ejemplo = """nombre,edad,ciudad
Ana,25,Madrid
Luis,30,Barcelona
María,28,Valencia"""

df = pd.read_csv(StringIO(csv_ejemplo))
print(df)

# Con archivo real: df = pd.read_csv("ruta/al_archivo.csv")
# Opciones útiles: sep=";", encoding="utf-8", header=0
