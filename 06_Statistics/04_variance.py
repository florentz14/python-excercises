# -------------------------------------------------
# File Name: 04_variance.py
# Author: Florentino Báez
# Description: Calculates population and sample variance and clarifies ddof=0 vs ddof=1 differences in NumPy.
# -------------------------------------------------

import statistics # Statistical functions
import numpy as np # Fast numerical operations

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40] # Data set

print("=== DATA ===")
print(data) # print the data set
print()

# Variance (population)
var_p = statistics.pvariance(data) # Variance (population)
print(f"Variance (population): {var_p:.2f}") # print the variance (population)

# Variance (sample)
var_s = statistics.variance(data) # Variance (sample)
print(f"Variance (sample): {var_s:.2f}") # print the variance (sample)
print()

# NumPy
print("=== NUMPY ===")
print(f"np.var (ddof=0, population): {np.var(data):.2f}") # NumPy variance (population)
print(f"np.var (ddof=1, sample): {np.var(data, ddof=1):.2f}") 