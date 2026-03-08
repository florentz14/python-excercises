# -------------------------------------------------
# File Name: 51_r_squared.py
# Description: Computes R-squared as explained variance proportion from residual and total variation.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Predictor variable
y = 2 + 3 * x + np.random.normal(0, 2, len(x))  # Response variable

slope, intercept, r, _, _ = stats.linregress(x, y)  # Estimated slope (beta1)
y_pred = intercept + slope * x  # Model predictions
ss_res = np.sum((y - y_pred)**2)  # Residual sum of squares
ss_tot = np.sum((y - np.mean(y))**2)  # Total sum of squares
r_squared = 1 - ss_res / ss_tot  # Explained variance proportion

print("=== R-SQUARED (coefficient of determination) ===")
print("R² = 1 - SS_res / SS_tot") # R² = 1 - SS_res / SS_tot
print("    = proportion of variance in y explained by x") # proportion of variance in y explained by x
print()
print(f"R² = {r_squared:.4f}") # print the R²
print(f"r² (Pearson squared) = {r**2:.4f}") # print the r² (Pearson squared)
print()
print("R² ∈ [0, 1]. Closer to 1 = better fit.") # R² ∈ [0, 1]. Closer to 1 = better fit.
