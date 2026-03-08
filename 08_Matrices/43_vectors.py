# -------------------------------------------------
# File Name: 43_vectors.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Add, scalar, dot product, norm.
# -------------------------------------------------

import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
k = 3

# Add
sum_vw = v + w
print("v =", v)
print("w =", w)
print("v + w =", sum_vw)

# Scalar
print("\nk * v =", k * v)

# Dot product
dot_result = np.dot(v, w)  # or v @ w
print("\nv · w =", dot_result)

# Norm (magnitude)
norm_v = np.linalg.norm(v)
print("||v|| =", norm_v)

# Subtract
print("v - w =", v - w)
