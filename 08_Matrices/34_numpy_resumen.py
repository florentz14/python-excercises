"""
NumPy - Paso 6: Resumen Python básico vs NumPy
==============================================
Tema: Python básico → NumPy paso a paso (08_Matrices)
Descripción: Tabla de equivalencias para repasar el paso a paso.
"""

import numpy as np

# ---------------------------------------------------------------------------
# VECTORES
# ---------------------------------------------------------------------------
# Python (listas)              |  NumPy (np.array)
# ----------------------------|------------------------------------------
# v = [1, 2, 3]               |  v = np.array([1, 2, 3])
# [v[i] + w[i] for i in ...]  |  v + w
# [k * x for x in v]          |  k * v
# sum(v[i]*w[i] for i in ...) |  np.dot(v, w)  o  v @ w
# math.sqrt(sum(x*x for x in v)) |  np.linalg.norm(v)
# len(v)                      |  v.shape  (ej: (3,))

# ---------------------------------------------------------------------------
# MATRICES
# ---------------------------------------------------------------------------
# Python (lista de listas)    |  NumPy
# ----------------------------|------------------------------------------
# A = [[1,2],[3,4]]           |  A = np.array([[1,2],[3,4]])
# loops para A+B               |  A + B
# loops para k*A              |  k * A
# transpuesta con list comp   |  A.T
# loops para A*B              |  A @ B  o  np.dot(A, B)
# len(A), len(A[0])           |  A.shape  (ej: (2, 2))

print("Resumen: ejecuta los archivos numpy_01 ... numpy_05 para ver cada paso.")
print("Ventajas de NumPy: sintaxis corta, rápido (C), muchas funciones (linalg, etc.).")
