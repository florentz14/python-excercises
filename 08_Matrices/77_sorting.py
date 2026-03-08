# -------------------------------------------------
# File Name: 77_sorting.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: In-place vs copy; get indices that would sort.
# -------------------------------------------------

import numpy as np

# 1D sort
v = np.array([30, 10, 50, 20, 40])
print("Original:", v)

# np.sort returns new array (does not modify v)
sorted_v = np.sort(v)
print("np.sort:", sorted_v)

# argsort: indices that would sort
idx = np.argsort(v)
print("argsort indices:", idx)
print("v[idx]:", v[idx])

# 2D: sort along axis
A = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print("\nMatrix:\n", A)
print("Sort each row (axis=1):\n", np.sort(A, axis=1))
print("Sort each column (axis=0):\n", np.sort(A, axis=0))

# In-place sort (1D only for ndarray)
v2 = np.array([5, 2, 8, 1])
v2.sort()
print("\nIn-place v.sort():", v2)
