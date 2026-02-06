"""
Pandas - Ejemplo 3: Filtrar filas (condiciones)
===============================================
Tema: Pandas (09_Pandas)
Descripción: df[condición] para quedarse con filas que cumplen la condición.
"""

import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "María", "Pedro"],
    "edad": [25, 30, 28, 35],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid"],
})

# Filtrar: edad >= 28
mayores = df[df["edad"] >= 28]
print("Edad >= 28:\n", mayores)

# Filtrar: ciudad == "Madrid"
madrid = df[df["ciudad"] == "Madrid"]
print("\nCiudad Madrid:\n", madrid)

# Combinar: (edad >= 28) y (ciudad == "Madrid")
filtro = df[(df["edad"] >= 28) & (df["ciudad"] == "Madrid")]
print("\nEdad >= 28 y Madrid:\n", filtro)
