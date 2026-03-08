# -------------------------------------------------
# File Name: 16_standardization.py
# Author: Florentino Báez
# Description: Applies standardization (mean=0, std=1) and verifies transformed-data properties.
# -------------------------------------------------

import numpy as np # Fast numerical operations

data = np.array([10, 12, 14, 15, 16, 18, 20, 100]) # Data set

print("=== DATA ===")
print(data) # Data set
print()

# Standardization
mean = np.mean(data) # Mean
std = np.std(data, ddof=1) # Standard deviation with Bessel's correction
standardized = (data - mean) / std # Standardized data

print("=== STANDARDIZED DATA ===")
print(standardized) # Standardized data
print(f"Mean: {np.mean(standardized):.4f}, Std: {np.std(standardized, ddof=1):.4f}") # Mean and standard deviation of the standardized data
