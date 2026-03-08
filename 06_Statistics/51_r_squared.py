# -------------------------------------------------
# File Name: 51_r_squared.py
# Description: Computes R-squared as explained variance proportion from residual and total variation.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = 2 + 3 * x + np.random.normal(0, 2, len(x))

slope, intercept, r, _, _ = stats.linregress(x, y)
y_pred = intercept + slope * x
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - ss_res / ss_tot

print("=== R-SQUARED (coefficient of determination) ===")
print("R² = 1 - SS_res / SS_tot")
print("    = proportion of variance in y explained by x")
print()
print(f"R² = {r_squared:.4f}")
print(f"r² (Pearson squared) = {r**2:.4f}")
print()
print("R² ∈ [0, 1]. Closer to 1 = better fit.")
