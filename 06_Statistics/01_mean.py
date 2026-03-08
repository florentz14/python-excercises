# -------------------------------------------------
# File Name: 01_mean.py
# Author: Florentino Báez
# Description: Computes the arithmetic mean of a dataset and compares results using statistics.mean and numpy.mean.
# -------------------------------------------------

import statistics  # Statistical functions
import numpy as np  # Numerical arrays and vectorized operations

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40] # Data set

print("=== DATA ===")
print(data) # print the data set
print()

# Mean (statistics)
mean = statistics.mean(data) # Mean
print(f"Mean (average): {mean:.2f}") # print the mean (average)
print()

# NumPy
print("=== NUMPY ===")
print(f"np.mean: {np.mean(data):.2f}") # print the NumPy mean
