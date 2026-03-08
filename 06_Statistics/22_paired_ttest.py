# -------------------------------------------------
# File Name: 22_paired_ttest.py
# Author: Florentino Báez
# Description: T-test pareado (before/after).
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
before = np.random.normal(50, 10, 20)
after = before + np.random.normal(5, 3, 20)

t_stat, p_value = stats.ttest_rel(after, before)
print("=== PAIRED T-TEST (before vs after) ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
