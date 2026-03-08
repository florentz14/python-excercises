# -------------------------------------------------
# File Name: 47_linalg.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: np.dot, np.linalg.norm, np.linalg.inv (inverse).
# -------------------------------------------------

import numpy as np

# Dot product and norm
v = np.array([3.0, 4.0])
print("v =", v)
print("np.dot(v, v) =", np.dot(v, v))
print("np.linalg.norm(v) =", np.linalg.norm(v))

# Matrix inverse (square, non-singular only)
A = np.array([[1.0, 2.0], [3.0, 4.0]])
print("\nA =\n", A)

try:
    A_inv = np.linalg.inv(A)
    print("A^(-1) =\n", A_inv)
    print("A @ A^(-1) ≈ I\n", A @ A_inv)
except np.linalg.LinAlgError as e:
    print("No inverse (singular matrix):", e)

# Note: if det(A) = 0, inverse doesn't exist → LinAlgError
# B = np.array([[1, 2], [2, 4]])  # singular
