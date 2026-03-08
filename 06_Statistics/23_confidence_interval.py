# -------------------------------------------------
# File Name: 23_confidence_interval.py
# Author: Florentino Báez
# Description: Computes a confidence interval for the mean using the t distribution and standard error.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
group_a = np.random.normal(100, 15, 30)

# 95% Confidence interval for mean
ci = stats.t.interval(0.95, len(group_a) - 1, loc=np.mean(group_a), scale=stats.sem(group_a))

print("=== 95% CONFIDENCE INTERVAL (mean of A) ===")
print(f"CI: [{ci[0]:.2f}, {ci[1]:.2f}]")
print(f"Sample mean: {np.mean(group_a):.2f}")
