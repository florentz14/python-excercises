# -------------------------------------------------
# File Name: 48_wilcoxon_test.py
# Description: Runs Wilcoxon signed-rank test as a non-parametric alternative for paired samples.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
before = np.random.exponential(2, 20)
after = before + np.random.normal(1, 0.5, 20)

stat, p_val = stats.wilcoxon(before, after, alternative='two-sided')

print("=== WILCOXON SIGNED-RANK TEST ===")
print("Non-parametric alternative to paired t-test")
print()
print(f"Before mean: {np.mean(before):.2f}")
print(f"After mean: {np.mean(after):.2f}")
print()
print(f"Statistic: {stat}")
print(f"p-value: {p_val:.4f}")
print(f"Reject H0 (no difference): {p_val < 0.05}")
