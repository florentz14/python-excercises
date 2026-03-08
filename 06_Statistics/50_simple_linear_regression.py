# -------------------------------------------------
# File Name: 50_simple_linear_regression.py
# Description: Regresión lineal simple.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = 2 + 3 * x + np.random.normal(0, 2, len(x))

slope, intercept, r, p_val, se = stats.linregress(x, y)

print("=== SIMPLE LINEAR REGRESSION ===")
print("y = β0 + β1*x + ε")
print()
print(f"Intercept (β0): {intercept:.2f}")
print(f"Slope (β1): {slope:.2f}")
print(f"Correlation r: {r:.4f}")
print(f"p-value (slope=0): {p_val:.4f}")
print()
print("Predicted: y =", f"{intercept:.2f} + {slope:.2f}*x")
