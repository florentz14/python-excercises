"""
Pandas - Ejemplo 4: Seleccionar y crear columnas
================================================
Tema: Pandas (09_Pandas)
Descripción: df["col"], df[["col1","col2"]], df["nueva"] = ... para columnas.
"""

import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "María"],
    "edad": [25, 30, 28],
    "saldo": [100, 200, 150],
})

# Una columna (Series)
print("Columna 'edad':\n", df["edad"])

# Varias columnas (DataFrame)
print("\nColumnas nombre y edad:\n", df[["nombre", "edad"]])

# Nueva columna
df["doble_saldo"] = df["saldo"] * 2
print("\nDataFrame con nueva columna:\n", df)
