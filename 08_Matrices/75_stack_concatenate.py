# -------------------------------------------------
# File Name: 75_stack_concatenate.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: vstack, hstack, concatenate, split.
# -------------------------------------------------

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A:\n", A)
print("B:\n", B)

# Vertical stack: one above the other
vstack = np.vstack([A, B])
print("\nvstack (vertical):\n", vstack)

# Horizontal stack: side by side
hstack = np.hstack([A, B])
print("hstack (horizontal):\n", hstack)

# Concatenate along axis
conc0 = np.concatenate([A, B], axis=0)  # along rows
conc1 = np.concatenate([A, B], axis=1)  # along cols
print("\nconcatenate axis=0:\n", conc0)
print("concatenate axis=1:\n", conc1)

# Split
rows = np.split(vstack, 2)
print("\nsplit vstack into 2:\n", rows[0], "\n", rows[1])
