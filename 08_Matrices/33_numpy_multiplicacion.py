"""
NumPy - Paso 5: Multiplicación de matrices y matriz × vector
=============================================================
Tema: Python básico → NumPy paso a paso (08_Matrices)
Descripción: A @ B, np.dot(A, B) y matriz por vector.
Equivalente en Python: matrix_05 (A*B), matrix_06 (A*v).
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices: operador @ (Python 3.5+)
C = A @ B
print("A =\n", A)
print("B =\n", B)
print("A @ B =\n", C)

# Alternativa: np.matmul(A, B) o np.dot(A, B)

# Matriz × vector (columna)
M = np.array([[1, 2], [3, 4], [5, 6]])  # 3×2
v = np.array([7, 8])                      # vector (2,)
resultado = M @ v   # resultado: vector de 3 componentes
print("\nM =\n", M)
print("v =", v)
print("M @ v =", resultado)
