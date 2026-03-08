# -------------------------------------------------
# File Name: 21_two_sample_ttest.py
# Author: Florentino Báez
# Description: Runs an independent two-sample t-test to evaluate mean differences between two groups.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
group_a = np.random.normal(100, 15, 30)
group_b = np.random.normal(105, 15, 30)

print("=== GROUPS ===")
print(f"Group A: mean={np.mean(group_a):.2f}, std={np.std(group_a, ddof=1):.2f}")
print(f"Group B: mean={np.mean(group_b):.2f}, std={np.std(group_b, ddof=1):.2f}")
print()

# Two-sample t-test (H0: means equal)
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print("=== TWO-SAMPLE T-TEST (H0: mean_A = mean_B) ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
