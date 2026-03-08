# -------------------------------------------------
# File Name: 49_anova_one_way.py
# Description: ANOVA de un factor.
# -------------------------------------------------

import numpy as np
from scipy import stats

np.random.seed(42)
group_a = np.random.normal(50, 10, 30)
group_b = np.random.normal(55, 10, 30)
group_c = np.random.normal(52, 10, 30)

f_stat, p_val = stats.f_oneway(group_a, group_b, group_c)

print("=== ONE-WAY ANOVA ===")
print("H0: all group means equal")
print("H1: at least one mean differs")
print()
print(f"Group A mean: {np.mean(group_a):.2f}")
print(f"Group B mean: {np.mean(group_b):.2f}")
print(f"Group C mean: {np.mean(group_c):.2f}")
print()
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_val:.4f}")
print(f"Reject H0: {p_val < 0.05}")
