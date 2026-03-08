# -------------------------------------------------
# File Name: 41_null_alternative_hypothesis.py
# Description: Defines null/alternative hypotheses and demonstrates decision-making with a one-sample t-test.
# -------------------------------------------------

from scipy import stats  # Statistical tests and probability distributions
import numpy as np  # Numerical arrays and vectorized operations

np.random.seed(42)  # Reproducible random results
sample = np.random.normal(102, 15, 30) # Sample

# H0: mean = 100 (null)
# H1: mean != 100 (alternative, two-sided)
t_stat, p_val = stats.ttest_1samp(sample, 100)  # Test statistic

print("=== NULL AND ALTERNATIVE HYPOTHESIS ===")
print("H0 (null): population mean = 100") # H0 (null): population mean = 100
print("H1 (alternative): population mean ≠ 100 (two-sided)") # H1 (alternative): population mean ≠ 100 (two-sided)  
print()
print(f"Sample mean: {np.mean(sample):.2f}") # print the sample mean
print(f"t-statistic: {t_stat:.4f}") # print the t-statistic
print(f"p-value: {p_val:.4f}") # print the p-value
print()
print("Decision at alpha=0.05:") # Decision at alpha=0.05:
print(f"  Reject H0: {p_val < 0.05}") # print the reject H0
