# -------------------------------------------------
# File Name: 32_spearman_correlation.py
# Description: Computes Spearman rank correlation for monotonic, potentially non-linear relationships.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

# Non-linear but monotonic relationship
x = np.array([1, 2, 3, 4, 5])  # Predictor variable
y = np.array([1, 4, 9, 16, 25])  # y = x^2

print("=== DATA (non-linear: y = x^2) ===")
print("x:", x) # print the x values
print("y:", y) # print the y values
print()

# Spearman: rank-based, robust to non-linearity
rho, p_val = stats.spearmanr(x, y) # Spearman correlation
print("=== SPEARMAN CORRELATION ===")
print(f"rho: {rho:.4f}") # print the Spearman correlation
print(f"p-value: {p_val:.4f}") # print the p-value  
print("Use when: ordinal data, non-linear but monotonic relationship, non-normal.")
