# -------------------------------------------------
# File Name: 36_gaussian_elimination.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Forward elimination to upper triangular, then back substitution.
# -------------------------------------------------

import numpy as np

def gaussian_elimination(A, b):
    """Solve Ax = b by Gaussian elimination. Returns x."""
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1)])
    n = len(Ab)
    for col in range(n):
        pivot = Ab[col, col]
        if abs(pivot) < 1e-10:
            raise ValueError("Singular matrix")
        Ab[col] /= pivot
        for row in range(col + 1, n):
            Ab[row] -= Ab[row, col] * Ab[col]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])
    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])
x = gaussian_elimination(A, b)
print("A:\n", A)
print("b:", b)
print("x:", x)
print("Check Ax = b:", np.allclose(A @ x, b))
