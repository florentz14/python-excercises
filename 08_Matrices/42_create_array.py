# ------------------------------------------------------------
# File: 30_numpy_create_array.py
# Purpose: Create NumPy arrays from lists.
# Description: Lists → np.array; .shape and .dtype.
# ------------------------------------------------------------

import numpy as np

# Vector: list → 1D array
lista_v = [1, 2, 3]
v = np.array(lista_v)
print("List:", lista_v)
print("Array v:", v)
print("  shape:", v.shape)  # (3,) = 1 row, 3 elements
print("  dtype:", v.dtype)

# Matrix: list of lists → 2D array
lista_A = [[1, 2, 3], [4, 5, 6]]
A = np.array(lista_A)
print("\nList of lists:", lista_A)
print("Array A:\n", A)
print("  shape:", A.shape)  # (2, 3) = 2 rows, 3 cols
print("  dtype:", A.dtype)

# Direct creation
zeros = np.zeros((2, 3))  # 2×3 zeros
ones = np.ones((2, 2))    # 2×2 ones
print("\nnp.zeros((2,3)):\n", zeros)
print("np.ones((2,2)):\n", ones)
