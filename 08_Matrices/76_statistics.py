# -------------------------------------------------
# File Name: 76_statistics.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Aggregate along axis (0=columns, 1=rows) or whole array.
# -------------------------------------------------

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix A:\n", A)

# Whole array
print("\n--- Whole array ---")
print("sum:", np.sum(A))
print("mean:", np.mean(A))
print("min:", np.min(A), "max:", np.max(A))
print("std:", np.std(A))

# Along axis: 0 = down columns, 1 = across rows
print("\n--- Axis 0 (per column) ---")
print("sum:", np.sum(A, axis=0))
print("mean:", np.mean(A, axis=0))

print("\n--- Axis 1 (per row) ---")
print("sum:", np.sum(A, axis=1))
print("mean:", np.mean(A, axis=1))

# Alternative: .sum(), .mean() as methods
print("\nA.sum():", A.sum())
print("A.mean(axis=1):", A.mean(axis=1))
