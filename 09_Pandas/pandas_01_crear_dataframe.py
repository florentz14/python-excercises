"""
Pandas - Ejemplo 1: Crear un DataFrame (tabla tipo Excel)
===========================================================
Tema: Pandas (09_Pandas)
Descripción: DataFrame desde un diccionario: columnas = claves, filas = valores.
"""

import pandas as pd

# Diccionario: clave = nombre de columna, valor = lista de filas
datos = {
    "nombre": ["Ana", "Luis", "María"],
    "edad": [25, 30, 28],
    "ciudad": ["Madrid", "Barcelona", "Valencia"],
}

df = pd.DataFrame(datos)
print(df)
print("\nColumnas:", df.columns.tolist())
print("Dimensiones:", df.shape)  # (filas, columnas)
