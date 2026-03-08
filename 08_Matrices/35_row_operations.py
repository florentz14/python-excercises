# -------------------------------------------------
# File Name: 35_row_operations.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Swap rows, scale row, row replacement (Ri += k*Rj).
# -------------------------------------------------

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print("Original A:\n", A)

# Swap rows 0 and 1
A_swap = A.copy()
A_swap[[0, 1]] = A_swap[[1, 0]]
print("\nSwap R0 <-> R1:\n", A_swap)

# Scale row 1 by 2
A_scale = A.copy()
A_scale[1] *= 2
print("\nScale R1 by 2:\n", A_scale)

# Row replacement: R2 = R2 + (-2)*R0
A_replace = A.copy()
A_replace[2] = A_replace[2] + (-2) * A_replace[0]
print("\nR2 = R2 - 2*R0:\n", A_replace)
