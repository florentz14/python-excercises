# -------------------------------------------------
# File Name: 05_standard_deviation.py
# Author: Florentino Báez
# Description: Calculates population and sample standard deviation to quantify spread around the mean.
# -------------------------------------------------

# Standard library and NumPy implementations
import statistics  # Built-in descriptive stats
import numpy as np  # Fast numerical operations

data = [12, 15, 18, 22, 25, 25, 28, 30, 33, 40] # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Standard deviation
std_p = statistics.pstdev(data) # Standard deviation (population)
std_s = statistics.stdev(data) # Standard deviation (sample)
print(f"Std dev (population): {std_p:.2f}")
print(f"Std dev (sample): {std_s:.2f}")
print()

# NumPy
print("=== NUMPY ===")
print(f"np.std (ddof=0): {np.std(data):.2f}") # NumPy standard deviation (population)
print(f"np.std (ddof=1, sample): {np.std(data, ddof=1):.2f}") # NumPy standard deviation (sample)
