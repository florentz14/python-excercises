# -------------------------------------------------
# File Name: 01_mean.py
# Author: Florentino Báez
# Description: Computes the arithmetic mean of a dataset and compares results using statistics.mean and numpy.mean.
# -------------------------------------------------

import statistics
import numpy as np

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40]

print("=== DATA ===")
print(data)
print()

# Mean (statistics)
mean = statistics.mean(data)
print(f"Mean (average): {mean:.2f}")
print()

# NumPy
print("=== NUMPY ===")
print(f"np.mean: {np.mean(data):.2f}")
