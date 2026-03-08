# -------------------------------------------------
# File Name: 32_spearman_correlation.py
# Description: Correlación de Spearman (ordinal, monotónica).
# -------------------------------------------------

import numpy as np
from scipy import stats

# Non-linear but monotonic relationship
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])  # y = x^2

print("=== DATA (non-linear: y = x^2) ===")
print("x:", x)
print("y:", y)
print()

# Spearman: rank-based, robust to non-linearity
rho, p_val = stats.spearmanr(x, y)
print("=== SPEARMAN CORRELATION ===")
print(f"rho: {rho:.4f}")
print(f"p-value: {p_val:.4f}")
print("Use when: ordinal data, non-linear but monotonic relationship, non-normal.")
