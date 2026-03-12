# -------------------------------------------------
# File Name: 47_binning_outliers_sampling.py
# Author: Florentino Baez
# Date: 12/03/2026
# Description: Binning, outlier detection, and random sampling.
# -------------------------------------------------

# Import numpy and pandas libraries
import numpy as np
import pandas as pd

# 1. Discretization (binning) (Series)
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

# Cut the ages into bins
cats = pd.cut(ages, bins)

# Cut the ages into quantiles
q_cats = pd.qcut(ages, 4)

# Print the cut categories
print("=== CUT (FIXED BINS) ===")
print(cats)

# Print the quantile categories
print("\n=== QCUT (QUANTILES) ===")
print(q_cats)

# Outlier detection
np.random.seed(7)

# Create a random DataFrame
randframe = pd.DataFrame(np.random.randn(1000, 3), columns=["A", "B", "C"])

# Detect outliers
outliers = randframe[(np.abs(randframe) > 3).any(axis=1)]

print("\n=== OUTLIER COUNT (|z| > 3 approx) ===")
print(len(outliers))
print("\nSample outliers:")
print(outliers.head().to_string(index=False))

# Permutation and random sampling
nframe = pd.DataFrame(np.arange(25).reshape(5, 5))

# Print the original DataFrame
print("=== ORIGINAL FRAME ===")
print(nframe)

# Permutation and random sampling
sampler = np.random.permutation(5)

# Take the shuffled DataFrame
shuffled_frame = nframe.take(sampler)

# Print the shuffled DataFrame
print("\n=== PERMUTATION AND RANDOM SAMPLING ===")
print("\n=== SHUFFLED FRAME ===")
print(shuffled_frame)
