# -------------------------------------------------
# File Name: 28_poisson_distribution.py
# Description: Uses the Poisson distribution to model event counts in fixed intervals.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

lambda_param = 3  # rate parameter (lambda)

print("=== POISSON (lambda=3) ===") # Poisson distribution (lambda=3)
print(f"P(X=2): {stats.poisson.pmf(2, lambda_param):.4f}") # print the probability of X=2
print(f"P(X <= 5): {stats.poisson.cdf(5, lambda_param):.4f}") # print the probability of X <= 5
print(f"Mean = Var = lambda: {lambda_param}") # print the mean = variance = lambda
print()

# Random samples
samples = np.random.poisson(lambda_param, 1000) # Random samples
print(f"Sample mean: {np.mean(samples):.2f}, sample var: {np.var(samples):.2f}") # print the sample mean and sample variance
