# -------------------------------------------------
# File Name: 13_correlation.py
# Author: Florentino Báez
# Description: Computes Pearson correlation, includes a negative-correlation example, and validates with a manual formula.
# -------------------------------------------------

import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])
y2 = np.array([55, 45, 35, 25, 15])

print("=== DATA ===")
print("x:", x)
print("y:", y)
print()

# Pearson correlation
corr = np.corrcoef(x, y)
print("=== CORRELATION MATRIX (Pearson) ===")
print(corr)
print(f"Corr(x,y): {np.corrcoef(x, y)[0, 1]:.4f}")
print()

# Manual: r = cov / (std_x * std_y)
cov_xy = np.cov(x, y, ddof=1)[0, 1]
std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)
r_manual = cov_xy / (std_x * std_y)
print("=== MANUAL: r = cov/(std_x * std_y) ===")
print(f"r = {r_manual:.4f}")
print()

# Negative correlation
r2 = np.corrcoef(x, y2)[0, 1]
print("=== NEGATIVE CORRELATION ===")
print(f"Corr(x, y2): {r2:.4f}")
print()

# Multiple variables
data = np.column_stack([x, y, y2])
corr_multi = np.corrcoef(data.T)
print("=== 3 VARIABLES CORRELATION ===")
print(corr_multi)
