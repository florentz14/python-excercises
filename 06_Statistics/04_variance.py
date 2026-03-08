# -------------------------------------------------
# File Name: 04_variance.py
# Author: Florentino Báez
# Description: Calculates population and sample variance and clarifies ddof=0 vs ddof=1 differences in NumPy.
# -------------------------------------------------

import statistics
import numpy as np

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Variance (population)
var_p = statistics.pvariance(data)
print(f"Variance (population): {var_p:.2f}")

# Variance (sample)
var_s = statistics.variance(data)
print(f"Variance (sample): {var_s:.2f}")
print()

# NumPy
print("=== NUMPY ===")
print(f"np.var (ddof=0, population): {np.var(data):.2f}")
print(f"np.var (ddof=1, sample): {np.var(data, ddof=1):.2f}")
