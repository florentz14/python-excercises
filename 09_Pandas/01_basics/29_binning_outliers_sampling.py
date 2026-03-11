# -------------------------------------------------
# File Name: 29_binning_outliers_sampling.py
# Author: Florentino Baez
# Date: 09_Pandas
# Description: Binning, outlier detection, and random sampling.
# -------------------------------------------------

import numpy as np
import pandas as pd

# 1. Discretization (binning) (Series)
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
q_cats = pd.qcut(ages, 4)

print("=== CUT (FIXED BINS) ===")
print(cats)
print("\n=== QCUT (QUANTILES) ===")
print(q_cats)

# 2. Outlier detection (DataFrame)
np.random.seed(7)
randframe = pd.DataFrame(np.random.randn(1000, 3), columns=["A", "B", "C"])
outliers = randframe[(np.abs(randframe) > 3).any(axis=1)]

print("\n=== OUTLIER COUNT (|z| > 3 approx) ===")
print(len(outliers))
print("\nSample outliers:")
print(outliers.head().to_string(index=False))

# 3. Permutation and random sampling (DataFrame)
nframe = pd.DataFrame(np.arange(25).reshape(5, 5))
# Print the DataFrame
print("=== ORIGINAL FRAME ===")
print(nframe)
# Permutation and random sampling (DataFrame)
sampler = np.random.permutation(5)
shuffled_frame = nframe.take(sampler)
# Print the shuffled DataFrame
print("\n=== SHUFFLED FRAME ===")
print(shuffled_frame)
