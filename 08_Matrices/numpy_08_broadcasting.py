"""
NumPy - Broadcasting
====================
Tema: 08_Matrices - Reglas para operar arrays de distintas formas
Descripción: NumPy "expande" dimensiones para permitir v + escalar, matriz + vector, etc.
"""

import numpy as np

# Vector + escalar: el escalar se aplica a cada elemento
v = np.array([1, 2, 3])
print("v =", v)
print("v + 10 =", v + 10)

# Matriz + vector (fila): cada fila de la matriz + el vector
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2×3
b = np.array([10, 20, 30])              # (3,)
print("\nA =\n", A)
print("b =", b)
print("A + b =\n", A + b)  # b se "repite" en cada fila

# Matriz × vector columna (broadcasting)
col = np.array([[1], [2]])  # 2×1
print("\ncol =", col.T)
print("A + col =\n", A + col)  # col se repite en cada columna de A
