# -------------------------------------------------
# File Name: 42_p_value.py
# Description: Explains and computes p-value interpretation against a chosen significance level alpha.
# -------------------------------------------------

from scipy import stats
import numpy as np

np.random.seed(42)
sample = np.random.normal(100, 15, 30)
t_stat, p_value = stats.ttest_1samp(sample, 100)

print("=== P-VALUE ===")
print("p-value = probability of observing data at least as extreme")
print("         as ours, assuming H0 is true.")
print()
print(f"Sample mean: {np.mean(sample):.2f}")
print(f"Test (H0: mean=100): t={t_stat:.4f}, p={p_value:.4f}")
print()
print("Interpretation:")
print("  p < 0.05: reject H0 (evidence against null)")
print("  p >= 0.05: fail to reject H0")
print()
print(f"This sample: p={'<' if p_value < 0.05 else '>='} 0.05")
