# -------------------------------------------------
# File Name: 47_mann_whitney_u.py
# Description: Prueba Mann-Whitney U (no paramétrica, dos grupos independientes).
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
group_a = np.random.exponential(2, 25)
group_b = np.random.exponential(3, 25)

stat, p_val = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')

print("=== MANN-WHITNEY U TEST ===")
print("Non-parametric alternative to two-sample t-test")
print()
print(f"Group A mean: {np.mean(group_a):.2f}")
print(f"Group B mean: {np.mean(group_b):.2f}")
print()
print(f"Statistic: {stat}")
print(f"p-value: {p_val:.4f}")
print(f"Reject H0 (distributions equal): {p_val < 0.05}")
