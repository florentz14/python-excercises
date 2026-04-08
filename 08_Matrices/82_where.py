# -------------------------------------------------
# File Name: 82_where.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: np.where for indices and per-element conditional replacement.
# See also: 78_bool_ix.py
# -------------------------------------------------

import numpy as np

v = np.array([1, 5, 3, 8, 2, 9, 4])
print("Array:", v)

# np.where: indices where condition is True
idx = np.where(v > 4)
print("np.where(v > 4):", idx[0])

# np.where(cond, x, y): choose x or y per element
replaced = np.where(v % 2 == 0, 0, v)
print("Replace evens with 0:", replaced)
