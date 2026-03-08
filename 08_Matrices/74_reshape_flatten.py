# -------------------------------------------------
# File Name: 74_reshape_flatten.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: reshape(), flatten(), ravel(); -1 for auto dimension.
# -------------------------------------------------

import numpy as np

# Create 1D array
v = np.array([1, 2, 3, 4, 5, 6])
print("1D:", v, "shape:", v.shape)

# Reshape to 2x3 (row-major order)
A = v.reshape(2, 3)
print("\nReshape (2, 3):\n", A)

# Reshape to 3x2 (auto one dim with -1)
B = v.reshape(3, -1)
print("Reshape (3, -1):\n", B)

# Flatten: 2D → 1D (always copy)
flat = A.flatten()
print("\nFlatten:", flat)

# Ravel: 2D → 1D (view when possible)
rav = A.ravel()
print("Ravel:", rav)

# Reshape in place (if contiguous)
v2 = np.arange(12)
M = v2.reshape(3, 4)
print("\n3x4 matrix:\n", M)
