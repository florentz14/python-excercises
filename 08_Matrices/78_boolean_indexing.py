# -------------------------------------------------
# File Name: 78_boolean_indexing.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Comparison operators, logical AND/OR, where().
# -------------------------------------------------

import numpy as np

v = np.array([1, 5, 3, 8, 2, 9, 4])
print("Array:", v)

# Boolean mask: elements > 4
mask = v > 4
print("Mask (v > 4):", mask)
print("v[mask]:", v[mask])

# Shorthand: v[v > 4]
print("v[v > 4]:", v[v > 4])

# Multiple conditions: AND with &, OR with |
print("v[(v > 2) & (v < 7)]:", v[(v > 2) & (v < 7)])
print("v[(v < 3) | (v > 6)]:", v[(v < 3) | (v > 6)])

# np.where: indices where condition is True
idx = np.where(v > 4)
print("np.where(v > 4):", idx[0])

# np.where(cond, x, y): choose x or y per element
replaced = np.where(v % 2 == 0, 0, v)
print("Replace evens with 0:", replaced)
