"""
NumPy - Paso 2: Crear arrays desde listas
==========================================
Tema: Python básico → NumPy paso a paso (08_Matrices)
Descripción: Convertir listas en np.array; .shape y .dtype.
Equivalente en Python básico: vector_01, matrix_01 (listas).
"""

import numpy as np

# --- Vector (lista → array 1D) ---
lista_v = [1, 2, 3]
v = np.array(lista_v)
print("Lista:", lista_v)
print("Array v:", v)
print("  shape:", v.shape)   # (3,) = 1 fila, 3 elementos
print("  dtype:", v.dtype)   # tipo de dato (int, float64, etc.)

# --- Matriz (lista de listas → array 2D) ---
lista_A = [[1, 2, 3], [4, 5, 6]]
A = np.array(lista_A)
print("\nLista de listas:", lista_A)
print("Array A:\n", A)
print("  shape:", A.shape)   # (2, 3) = 2 filas, 3 columnas
print("  dtype:", A.dtype)

# --- Crear arrays directos ---
ceros = np.zeros((2, 3))   # matriz 2×3 de ceros
unos = np.ones((2, 2))    # matriz 2×2 de unos
print("\nnp.zeros((2,3)):\n", ceros)
print("np.ones((2,2)):\n", unos)
