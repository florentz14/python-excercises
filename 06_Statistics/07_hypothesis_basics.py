# -------------------------------------------------
# File Name: 07_hypothesis_basics.py
# Author: Florentino Báez
# Date: Statistics
# Description: Hypothesis testing basics, p-value, t-test.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)

# Two groups
group_a = np.random.normal(100, 15, 30)
group_b = np.random.normal(105, 15, 30)

print("=== GROUPS ===")
print(f"Group A: mean={np.mean(group_a):.2f}, std={np.std(group_a, ddof=1):.2f}")
print(f"Group B: mean={np.mean(group_b):.2f}, std={np.std(group_b, ddof=1):.2f}")
print()

# One-sample t-test (H0: mean = 100)
t_stat, p_value = stats.ttest_1samp(group_a, 100)
print("=== ONE-SAMPLE T-TEST (H0: mean=100) ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
print()

# Two-sample t-test (H0: means equal)
t_stat2, p_value2 = stats.ttest_ind(group_a, group_b)
print("=== TWO-SAMPLE T-TEST (H0: mean_A = mean_B) ===")
print(f"t-statistic: {t_stat2:.4f}")
print(f"p-value: {p_value2:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value2 < 0.05}")
print()

# Confidence interval for mean
ci = stats.t.interval(0.95, len(group_a) - 1, loc=np.mean(group_a), scale=stats.sem(group_a))
print("=== 95% CONFIDENCE INTERVAL (mean of A) ===")
print(f"CI: [{ci[0]:.2f}, {ci[1]:.2f}]")
print()

# Paired t-test (before/after)
before = np.random.normal(50, 10, 20)
after = before + np.random.normal(5, 3, 20)
t_paired, p_paired = stats.ttest_rel(after, before)
print("=== PAIRED T-TEST (before vs after) ===")
print(f"t-statistic: {t_paired:.4f}")
print(f"p-value: {p_paired:.4f}")
