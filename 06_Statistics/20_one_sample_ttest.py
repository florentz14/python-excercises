# -------------------------------------------------
# File Name: 20_one_sample_ttest.py
# Author: Florentino Báez
# Description: T-test de una muestra.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
group_a = np.random.normal(100, 15, 30)

print("=== GROUP ===")
print(f"Mean: {np.mean(group_a):.2f}, Std: {np.std(group_a, ddof=1):.2f}")
print()

# One-sample t-test (H0: mean = 100)
t_stat, p_value = stats.ttest_1samp(group_a, 100)
print("=== ONE-SAMPLE T-TEST (H0: mean=100) ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
