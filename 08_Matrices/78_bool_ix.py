# -------------------------------------------------
# File Name: 78_bool_ix.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Boolean masks, fancy indexing, logical AND/OR on arrays.
# See also: 82_where.py, 110_df_bool.py
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
