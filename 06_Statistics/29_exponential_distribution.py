# -------------------------------------------------
# File Name: 29_exponential_distribution.py
# Description: Uses the exponential distribution to model waiting times and tail probabilities.
# -------------------------------------------------

import numpy as np
from scipy import stats

scale = 2  # 1/lambda, mean = scale

print("=== EXPONENTIAL (scale=2) ===")
print(f"P(X <= 1): {stats.expon.cdf(1, scale=scale):.4f}")
print(f"P(X > 2): {1 - stats.expon.cdf(2, scale=scale):.4f}")
print(f"Mean = scale: {scale}")
print()

# Random samples
samples = np.random.exponential(scale, 1000)
print(f"Sample mean: {np.mean(samples):.2f}, expected: {scale}")
