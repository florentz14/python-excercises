"""
NumPy - Paso 3: Operaciones con vectores (arrays 1D)
====================================================
Tema: Python básico → NumPy paso a paso (08_Matrices)
Descripción: Suma, producto por escalar, producto punto y norma con NumPy.
Equivalente en Python: vector_02 (suma), vector_03 (escalar), vector_04 (punto), vector_05 (magnitud).
"""

import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
k = 3

# Suma: igual que listas pero con sintaxis directa
suma = v + w
print("v =", v)
print("w =", w)
print("v + w =", suma)

# Producto por escalar
print("\nk * v =", k * v)

# Producto punto (escalar)
producto_punto = np.dot(v, w)   # o v @ w en arrays 1D
print("\nv · w =", producto_punto)

# Magnitud (norma)
norma = np.linalg.norm(v)
print("||v|| =", norma)

# Resta
print("v - w =", v - w)
