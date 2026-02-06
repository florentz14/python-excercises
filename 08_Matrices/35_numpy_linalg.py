"""
NumPy - Álgebra lineal: dot, norm, inverse
===========================================
Tema: 08_Matrices - Siguiente paso después de arrays básicos
Descripción: np.dot, np.linalg.norm, np.linalg.inv. Inversa solo si existe (con cuidado).
"""

import numpy as np

# --- Producto punto y norma (ya vistos en numpy_03, numpy_05) ---
v = np.array([3.0, 4.0])
print("v =", v)
print("np.dot(v, v) =", np.dot(v, v))
print("np.linalg.norm(v) =", np.linalg.norm(v))

# --- Inversa de una matriz (con cuidado: solo matrices cuadradas no singulares) ---
A = np.array([[1.0, 2.0], [3.0, 4.0]])
print("\nA =\n", A)

try:
    A_inv = np.linalg.inv(A)
    print("A^(-1) =\n", A_inv)
    print("A @ A^(-1) =\n", A @ A_inv)  # Debería ser ~ I
except np.linalg.LinAlgError as e:
    print("No existe inversa (matriz singular):", e)

# Cuidado: si det(A) = 0, la inversa no existe → LinAlgError
# B = np.array([[1, 2], [2, 4]])  # singular, no invertible
