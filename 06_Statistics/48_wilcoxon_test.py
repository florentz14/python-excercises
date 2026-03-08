# -------------------------------------------------
# File Name: 48_wilcoxon_test.py
# Description: Runs Wilcoxon signed-rank test as a non-parametric alternative for paired samples.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
before = np.random.exponential(2, 20)  # Baseline paired measurements
after = before + np.random.normal(1, 0.5, 20)  # Follow-up paired measurements

stat, p_val = stats.wilcoxon(before, after, alternative='two-sided')  # Test statistic

print("=== WILCOXON SIGNED-RANK TEST ===")
print("Non-parametric alternative to paired t-test") # Non-parametric alternative to paired t-test  
print()
print(f"Before mean: {np.mean(before):.2f}") # print the before mean
print(f"After mean: {np.mean(after):.2f}") # print the after mean
print()
print(f"Statistic: {stat}") # print the statistic
print(f"p-value: {p_val:.4f}") # print the p-value
print(f"Reject H0 (no difference): {p_val < 0.05}") # print the reject H0 (no difference): {p_val < 0.05}
