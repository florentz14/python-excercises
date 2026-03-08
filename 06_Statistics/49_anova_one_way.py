# -------------------------------------------------
# File Name: 49_anova_one_way.py
# Description: Runs one-way ANOVA to compare means across three or more independent groups.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
group_a = np.random.normal(50, 10, 30)  # Simulated sample from group A
group_b = np.random.normal(55, 10, 30)  # Simulated sample from group B
group_c = np.random.normal(52, 10, 30) # Simulated sample from group C

f_stat, p_val = stats.f_oneway(group_a, group_b, group_c)  # ANOVA test statistic

print("=== ONE-WAY ANOVA ===")
print("H0: all group means equal") # H0: all group means equal
print("H1: at least one mean differs") # H1: at least one mean differs
print()
print(f"Group A mean: {np.mean(group_a):.2f}") # print the group A mean
print(f"Group B mean: {np.mean(group_b):.2f}") # print the group B mean
print(f"Group C mean: {np.mean(group_c):.2f}") # print the group C mean
print()
print(f"F-statistic: {f_stat:.4f}") # print the F-statistic
print(f"p-value: {p_val:.4f}") # print the p-value
print(f"Reject H0: {p_val < 0.05}") # print the reject H0: {p_val < 0.05}
