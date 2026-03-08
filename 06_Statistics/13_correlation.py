# -------------------------------------------------
# File Name: 13_correlation.py
# Author: Florentino Báez
# Description: Computes Pearson correlation, includes a negative-correlation example, and validates with a manual formula.
# -------------------------------------------------

import numpy as np # Fast numerical operations

x = np.array([10, 20, 30, 40, 50]) # Data set
y = np.array([15, 25, 35, 45, 55]) # Data set
y2 = np.array([55, 45, 35, 25, 15]) # Data set

print("=== DATA ===")
print("x:", x) # Data set
print("y:", y) # Data set
print()

# Pearson correlation
corr = np.corrcoef(x, y) # Pearson correlation
print("=== CORRELATION MATRIX (Pearson) ===")
print(corr) # Pearson correlation
print(f"Corr(x,y): {np.corrcoef(x, y)[0, 1]:.4f}")
print()

# Manual: r = cov / (std_x * std_y)
cov_xy = np.cov(x, y, ddof=1)[0, 1] # Covariance of x and y
std_x = np.std(x, ddof=1) # Standard deviation of x
std_y = np.std(y, ddof=1) # Standard deviation of y with Bessel's correction
r_manual = cov_xy / (std_x * std_y) # Pearson correlation
print("=== MANUAL: r = cov/(std_x * std_y) ===")
print(f"r = {r_manual:.4f}")
print()

# Negative correlation
r2 = np.corrcoef(x, y2)[0, 1] # Pearson correlation
print("=== NEGATIVE CORRELATION ===")
print(f"Corr(x, y2): {r2:.4f}")
print()

# Multiple variables
data = np.column_stack([x, y, y2]) # Data set
corr_multi = np.corrcoef(data.T) # Pearson correlation
print("=== 3 VARIABLES CORRELATION ===")
print(corr_multi) # Pearson correlation
