# -------------------------------------------------
# File Name: 01_descriptive_stats.py
# Author: Florentino Báez
# Date: Statistics
# Description: Mean, median, mode, variance, standard deviation.
# -------------------------------------------------

import statistics
import numpy as np

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Mean
mean = statistics.mean(data)
print(f"Mean (average): {mean:.2f}")
print()

# Median
median = statistics.median(data)
print(f"Median (middle value): {median}")
print()

# Mode
mode = statistics.mode(data)
print(f"Mode (most frequent): {mode}")
print()

# Variance (population)
var_p = statistics.pvariance(data)
print(f"Variance (population): {var_p:.2f}")

# Variance (sample)
var_s = statistics.variance(data)
print(f"Variance (sample): {var_s:.2f}")
print()

# Standard deviation
std_p = statistics.pstdev(data)
std_s = statistics.stdev(data)
print(f"Std dev (population): {std_p:.2f}")
print(f"Std dev (sample): {std_s:.2f}")
print()

# NumPy equivalents
print("=== NUMPY ===")
print(f"np.mean: {np.mean(data):.2f}")
print(f"np.median: {np.median(data):.2f}")
print(f"np.std (ddof=0): {np.std(data):.2f}")
print(f"np.std (ddof=1, sample): {np.std(data, ddof=1):.2f}")
print(f"np.var: {np.var(data):.2f}")
