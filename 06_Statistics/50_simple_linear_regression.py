# -------------------------------------------------
# File Name: 50_simple_linear_regression.py
# Description: Fits simple linear regression and reports slope, intercept, correlation, and significance.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Predictor variable
y = 2 + 3 * x + np.random.normal(0, 2, len(x))  # Response variable

slope, intercept, r, p_val, se = stats.linregress(x, y)  # Estimated slope (beta1)

print("=== SIMPLE LINEAR REGRESSION ===")
print("y = β0 + β1*x + ε") # y = β0 + β1*x + ε
print()
print(f"Intercept (β0): {intercept:.2f}") # print the intercept (β0)
print(f"Slope (β1): {slope:.2f}") # print the slope (β1)
print(f"Correlation r: {r:.4f}") # print the correlation r
print(f"p-value (slope=0): {p_val:.4f}") # print the p-value (slope=0)
print()
print("Predicted: y =", f"{intercept:.2f} + {slope:.2f}*x") # print the predicted: y = {intercept:.2f} + {slope:.2f}*x
