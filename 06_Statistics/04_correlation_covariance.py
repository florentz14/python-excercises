# -------------------------------------------------
# File Name: 04_correlation_covariance.py
# Author: Florentino Báez
# Date: Statistics
# Description: Correlation, covariance, scatter, Pearson.
# -------------------------------------------------

import numpy as np

# Two variables
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])

print("=== DATA ===")
print("x:", x)
print("y:", y)
print()

# Covariance
cov = np.cov(x, y)
print("=== COVARIANCE MATRIX (np.cov) ===")
print(cov)
print(f"Cov(x,y): {np.cov(x, y)[0, 1]:.2f}")
print()

# Pearson correlation
corr = np.corrcoef(x, y)
print("=== CORRELATION MATRIX (Pearson) ===")
print(corr)
print(f"Corr(x,y): {np.corrcoef(x, y)[0, 1]:.4f}")
print()

# Manual correlation: r = cov / (std_x * std_y)
cov_xy = np.cov(x, y, ddof=1)[0, 1]
std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)
r_manual = cov_xy / (std_x * std_y)
print("=== MANUAL: r = cov/(std_x * std_y) ===")
print(f"r = {r_manual:.4f}")
print()

# Negative correlation example
y2 = np.array([55, 45, 35, 25, 15])
r2 = np.corrcoef(x, y2)[0, 1]
print("=== NEGATIVE CORRELATION (y decreasing) ===")
print(f"Corr(x, y2): {r2:.4f}")
print()

# Multiple variables
data = np.column_stack([x, y, y2])
corr_multi = np.corrcoef(data.T)
print("=== 3 VARIABLES CORRELATION ===")
print(corr_multi)
