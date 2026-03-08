# -------------------------------------------------
# File Name: 28_poisson_distribution.py
# Description: Distribución de Poisson.
# -------------------------------------------------

import numpy as np
from scipy import stats

lambda_param = 3  # rate parameter

print("=== POISSON (lambda=3) ===")
print(f"P(X=2): {stats.poisson.pmf(2, lambda_param):.4f}")
print(f"P(X <= 5): {stats.poisson.cdf(5, lambda_param):.4f}")
print(f"Mean = Var = lambda: {lambda_param}")
print()

# Random samples
samples = np.random.poisson(lambda_param, 1000)
print(f"Sample mean: {np.mean(samples):.2f}, sample var: {np.var(samples):.2f}")
