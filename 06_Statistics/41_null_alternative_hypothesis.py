# -------------------------------------------------
# File Name: 41_null_alternative_hypothesis.py
# Description: Defines null/alternative hypotheses and demonstrates decision-making with a one-sample t-test.
# -------------------------------------------------

from scipy import stats
import numpy as np

np.random.seed(42)
sample = np.random.normal(102, 15, 30)

# H0: mean = 100 (null)
# H1: mean != 100 (alternative, two-sided)
t_stat, p_val = stats.ttest_1samp(sample, 100)

print("=== NULL AND ALTERNATIVE HYPOTHESIS ===")
print("H0 (null): population mean = 100")
print("H1 (alternative): population mean ≠ 100 (two-sided)")
print()
print(f"Sample mean: {np.mean(sample):.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")
print()
print("Decision at alpha=0.05:")
print(f"  Reject H0: {p_val < 0.05}")
