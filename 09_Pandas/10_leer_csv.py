"""
Pandas - Ejemplo 2: Leer un CSV (archivo tipo Excel)
====================================================
Tema: Pandas (09_Pandas)
Descripción: pd.read_csv() para cargar data.csv en un DataFrame.
"""

import pandas as pd
from pathlib import Path

# Ruta a data.csv en la raíz del proyecto (una carpeta arriba de 09_Pandas)
ruta_csv = Path(__file__).parent.parent / "data.csv"

df = pd.read_csv(ruta_csv, encoding="utf-8")
print(df)
print("\nColumnas:", df.columns.tolist())
print("Dimensiones:", df.shape)
print("\nPrimeras 5 filas:")
print(df.head())
