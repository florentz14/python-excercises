"""
NumPy - Paso 4: Operaciones con matrices (arrays 2D)
=====================================================
Tema: Python básico → NumPy paso a paso (08_Matrices)
Descripción: Suma, producto por escalar y transpuesta con NumPy.
Equivalente en Python: matrix_02 (suma), matrix_03 (escalar), matrix_04 (transpuesta).
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
k = 3

# Suma elemento a elemento
print("A =\n", A)
print("B =\n", B)
print("A + B =\n", A + B)

# Producto por escalar
print("\nk * A =\n", k * A)

# Transpuesta: .T (atributo)
print("A^T (transpuesta) =\n", A.T)

# Resta
print("A - B =\n", A - B)
