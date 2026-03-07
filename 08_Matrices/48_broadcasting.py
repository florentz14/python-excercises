# ------------------------------------------------------------
# File: 36_numpy_broadcasting.py
# Purpose: NumPy broadcasting.
# Description: Expand dimensions to allow v+scalar, matrix+vector, etc.
# ------------------------------------------------------------

import numpy as np

# Vector + scalar: scalar applied to each element
v = np.array([1, 2, 3])
print("v =", v)
print("v + 10 =", v + 10)

# Matrix + row vector: each row + vector
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2×3
b = np.array([10, 20, 30])            # (3,)
print("\nA =\n", A)
print("b =", b)
print("A + b =\n", A + b)  # b broadcast along rows

# Matrix + column vector
col = np.array([[1], [2]])  # 2×1
print("\ncol =", col.T)
print("A + col =\n", A + col)  # col broadcast along cols
