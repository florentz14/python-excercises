# -------------------------------------------------
# File Name: 12_covariance.py
# Author: Florentino Báez
# Description: Computes covariance matrix and cov(x,y) to assess joint variability between two variables.
# -------------------------------------------------

import numpy as np # Fast numerical operations

x = np.array([10, 20, 30, 40, 50]) # Data set
y = np.array([15, 25, 35, 45, 55]) # Data set

print("=== DATA ===")
print("x:", x) # Data set
print("y:", y) # Data set
print()

# Covariance matrix
cov = np.cov(x, y) # Covariance matrix
print("=== COVARIANCE MATRIX (np.cov) ===")
print(cov) # Covariance matrix
print(f"Cov(x,y): {np.cov(x, y)[0, 1]:.2f}") # Covariance of x and y
