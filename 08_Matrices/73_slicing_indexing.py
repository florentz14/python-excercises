# -------------------------------------------------
# File Name: 73_slicing_indexing.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: start:stop:step, negative indices, multi-dim slices.
# -------------------------------------------------

import numpy as np

# 1D array slicing
v = np.array([10, 20, 30, 40, 50, 60])
print("Array:", v)
print("v[1:4]:", v[1:4])       # indices 1, 2, 3
print("v[::2]:", v[::2])       # every 2nd element
print("v[-3:]:", v[-3:])       # last 3
print("v[::-1]:", v[::-1])      # reversed

# 2D array slicing
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\nMatrix A (3x4):\n", A)
print("A[1, :]:", A[1, :])           # row 1
print("A[:, 2]:", A[:, 2])           # column 2
print("A[0:2, 1:3]:\n", A[0:2, 1:3]) # submatrix rows 0-1, cols 1-2
print("A[::2, ::2]:\n", A[::2, ::2]) # every 2nd row and col
