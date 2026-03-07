# ------------------------------------------------------------
# File: 32_numpy_matrices.py
# Purpose: Matrix operations with NumPy.
# Description: Add, scalar, transpose, subtract.
# ------------------------------------------------------------

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
k = 3

# Element-wise add
print("A =\n", A)
print("B =\n", B)
print("A + B =\n", A + B)

# Scalar product
print("\nk * A =\n", k * A)

# Transpose: .T attribute
print("A^T (transpose) =\n", A.T)

# Subtract
print("A - B =\n", A - B)
