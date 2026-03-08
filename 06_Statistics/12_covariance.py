# -------------------------------------------------
# File Name: 12_covariance.py
# Author: Florentino Báez
# Description: Computes covariance matrix and cov(x,y) to assess joint variability between two variables.
# -------------------------------------------------

import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])

print("=== DATA ===")
print("x:", x)
print("y:", y)
print()

# Covariance matrix
cov = np.cov(x, y)
print("=== COVARIANCE MATRIX (np.cov) ===")
print(cov)
print(f"Cov(x,y): {np.cov(x, y)[0, 1]:.2f}")
