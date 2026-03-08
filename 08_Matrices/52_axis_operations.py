# -------------------------------------------------
# File Name: 52_axis_operations.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: axis=0 (columns), axis=1 (rows), axis=None (all).
# -------------------------------------------------

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:\n", arr)

print("\nSum all (axis=None):", arr.sum())
print("Sum per column (axis=0):", arr.sum(axis=0))
print("Sum per row (axis=1):", arr.sum(axis=1))

print("\nMean per column:", arr.mean(axis=0))
print("Max per row:", arr.max(axis=1))
print("Min per column:", arr.min(axis=0))
