# -------------------------------------------------
# File Name: 29_exponential_distribution.py
# Description: Uses the exponential distribution to model waiting times and tail probabilities.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

scale = 2  # 1/lambda, mean = scale (lambda = 1/scale)

print("=== EXPONENTIAL (scale=2) ===")
print(f"P(X <= 1): {stats.expon.cdf(1, scale=scale):.4f}") # print the probability of X <= 1
print(f"P(X > 2): {1 - stats.expon.cdf(2, scale=scale):.4f}") # print the probability of X > 2
print(f"Mean = scale: {scale}") # print the mean = scale
print()

# Random samples
samples = np.random.exponential(scale, 1000) # Random samples
print(f"Sample mean: {np.mean(samples):.2f}, expected: {scale}") # print the sample mean and expected
