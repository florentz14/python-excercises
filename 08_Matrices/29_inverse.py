# -------------------------------------------------
# File Name: 29_inverse.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Compute A^(-1) with np.linalg.inv. Check A @ A^(-1) = I.
# -------------------------------------------------

import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
A_inv = np.linalg.inv(A)
print("A:\n", A)
print("\nA^(-1):\n", A_inv)
print("\nA @ A^(-1) (should be I):\n", A @ A_inv)

# Singular matrix (no inverse)
B = np.array([[1.0, 2.0], [2.0, 4.0]])
try:
    B_inv = np.linalg.inv(B)
except np.linalg.LinAlgError as e:
    print("\nSingular matrix (no inverse):", e)
