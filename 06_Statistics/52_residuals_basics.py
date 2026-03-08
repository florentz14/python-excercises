# -------------------------------------------------
# File Name: 52_residuals_basics.py
# Description: Computes and interprets linear-model residuals, including mean, sum, and RMSE diagnostics.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Predictor variable
y = 2 + 3 * x + np.random.normal(0, 2, len(x))  # Response variable

slope, intercept, _, _, _ = stats.linregress(x, y)  # Estimated slope (beta1)
y_pred = intercept + slope * x  # Model predictions
residuals = y - y_pred  # Prediction errors

print("=== RESIDUALS ===")
print("residual = observed - predicted") # residual = observed - predicted
print()
print("Residuals (y - ŷ):") # Residuals (y - ŷ):
print(residuals.round(2)) # print the residuals
print()
print(f"Mean of residuals: {np.mean(residuals):.4f} (should ≈ 0)") # print the mean of residuals
print(f"Sum of residuals: {np.sum(residuals):.4f} (should ≈ 0)") # print the sum of residuals
print(f"RMSE: {np.sqrt(np.mean(residuals**2)):.2f}") # print the RMSE
print()
print("Check: residuals random, no pattern -> model assumptions OK") # Check: residuals random, no pattern -> model assumptions OK  
