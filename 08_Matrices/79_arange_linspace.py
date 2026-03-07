# ------------------------------------------------------------
# File: 50_array_arange_linspace.py
# Purpose: Create sequences: arange, linspace.
# Description: arange(start, stop, step); linspace for N evenly spaced values.
# ------------------------------------------------------------

import numpy as np

# arange: like range() but returns array
# arange(start, stop, step) - stop is exclusive
v1 = np.arange(0, 10, 2)
print("arange(0, 10, 2):", v1)  # [0, 2, 4, 6, 8]

v2 = np.arange(5)
print("arange(5):", v2)  # [0,1,2,3,4]

# linspace: N evenly spaced values from start to stop (inclusive)
v3 = np.linspace(0, 1, 5)
print("\nlinspace(0, 1, 5):", v3)  # [0, 0.25, 0.5, 0.75, 1]

# Useful for plots: 100 points from 0 to 2*pi
angles = np.linspace(0, 2 * np.pi, 100)
print("linspace(0, 2π, 100) length:", len(angles))

# 2D grid with mgrid or meshgrid
x = np.linspace(0, 2, 3)
y = np.linspace(0, 1, 2)
X, Y = np.meshgrid(x, y)
print("\nmeshgrid x:", x, "y:", y)
print("X:\n", X)
print("Y:\n", Y)
