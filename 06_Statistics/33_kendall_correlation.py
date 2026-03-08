# -------------------------------------------------
# File Name: 33_kendall_correlation.py
# Description: Computes Kendall tau correlation for ordinal association, robust with ties/small samples.
# -------------------------------------------------

import numpy as np
from scipy import stats

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 7, 8])

print("=== DATA ===")
print("x:", x)
print("y:", y)
print()

# Kendall tau: concordant vs discordant pairs
tau, p_val = stats.kendalltau(x, y)
print("=== KENDALL TAU ===")
print(f"tau: {tau:.4f}")
print(f"p-value: {p_val:.4f}")
print("Use when: ordinal data, many ties, small samples.")
