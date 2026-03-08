# -------------------------------------------------
# File Name: 52_residuals_basics.py
# Description: Computes and interprets linear-model residuals, including mean, sum, and RMSE diagnostics.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = 2 + 3 * x + np.random.normal(0, 2, len(x))

slope, intercept, _, _, _ = stats.linregress(x, y)
y_pred = intercept + slope * x
residuals = y - y_pred

print("=== RESIDUALS ===")
print("residual = observed - predicted")
print()
print("Residuals (y - ŷ):")
print(residuals.round(2))
print()
print(f"Mean of residuals: {np.mean(residuals):.4f} (should ≈ 0)")
print(f"Sum of residuals: {np.sum(residuals):.4f} (should ≈ 0)")
print(f"RMSE: {np.sqrt(np.mean(residuals**2)):.2f}")
print()
print("Check: residuals random, no pattern -> model assumptions OK")
