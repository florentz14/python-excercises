# -------------------------------------------------
# File Name: 33_kendall_correlation.py
# Description: Computes Kendall tau correlation for ordinal association, robust with ties/small samples.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

x = np.array([1, 2, 3, 4, 5])  # Predictor variable (x)
y = np.array([2, 4, 5, 7, 8])  # Response variable (y)  

print("=== DATA ===")
print("x:", x) # print the x values
print("y:", y) # print the y values
print()

# Kendall tau: concordant vs discordant pairs
tau, p_val = stats.kendalltau(x, y) # Kendall tau correlation
print("=== KENDALL TAU ===")
print(f"tau: {tau:.4f}") # print the Kendall tau correlation
print(f"p-value: {p_val:.4f}") # print the p-value  
print("Use when: ordinal data, many ties, small samples.")
