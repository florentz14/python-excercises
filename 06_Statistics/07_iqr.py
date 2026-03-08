# -------------------------------------------------
# File Name: 07_iqr.py
# Author: Florentino Báez
# Description: Computes IQR (Q3-Q1) and a five-number summary to describe central spread and robustness to outliers.
# -------------------------------------------------

# Standard library and NumPy implementations
import numpy as np  # Fast numerical operations

data = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) # Data set

print("=== DATA ===")
print(data) # Data set
print()

# IQR (Interquartile Range)
q1, q3 = np.percentile(data, [25, 75]) # Q1 and Q3
iqr = q3 - q1 # IQR
print("=== IQR ===")
print(f"Q1: {q1}, Q3: {q3}") # Q1 and Q3
print(f"IQR = Q3 - Q1 = {iqr}") # IQR
print()

# Five-number summary
print("=== FIVE-NUMBER SUMMARY ===")
print(f"Min: {np.min(data)}") # Min
print(f"Q1: {q1}") # Q1
print(f"Median: {np.median(data)}") # Median
print(f"Q3: {q3}") # Q3
print(f"Max: {np.max(data)}") # Max
