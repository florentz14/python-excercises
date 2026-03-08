# -------------------------------------------------
# File Name: 22_paired_ttest.py
# Author: Florentino Báez
# Description: Runs a paired t-test for before/after dependent measurements.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
before = np.random.normal(50, 10, 20)  # Baseline paired measurements
after = before + np.random.normal(5, 3, 20)  # Follow-up paired measurements

t_stat, p_value = stats.ttest_rel(after, before)  # Test statistic
print("=== PAIRED T-TEST (before vs after) ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
