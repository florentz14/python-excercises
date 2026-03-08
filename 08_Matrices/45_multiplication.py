# -------------------------------------------------
# File Name: 45_multiplication.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: A @ B, np.dot; matrix times column vector.
# -------------------------------------------------

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix product: @ operator (Python 3.5+)
C = A @ B
print("A =\n", A)
print("B =\n", B)
print("A @ B =\n", C)
# Alternatives: np.matmul(A, B) or np.dot(A, B)

# Matrix × column vector
M = np.array([[1, 2], [3, 4], [5, 6]])  # 3×2
v = np.array([7, 8])  # (2,)
result = M @ v  # result: 3-component vector
print("\nM =\n", M)
print("v =", v)
print("M @ v =", result)
