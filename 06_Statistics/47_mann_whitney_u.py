# -------------------------------------------------
# File Name: 47_mann_whitney_u.py
# Description: Runs Mann-Whitney U test as a non-parametric alternative for two independent groups.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

np.random.seed(42)  # Reproducible random results
group_a = np.random.exponential(2, 25)  # Simulated sample from group A
group_b = np.random.exponential(3, 25)  # Simulated sample from group B

stat, p_val = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')  # Test statistic

print("=== MANN-WHITNEY U TEST ===")
print("Non-parametric alternative to two-sample t-test") # Non-parametric alternative to two-sample t-test
print()
print(f"Group A mean: {np.mean(group_a):.2f}") # print the group A mean
print(f"Group B mean: {np.mean(group_b):.2f}") # print the group B mean
print()
print(f"Statistic: {stat}") # print the statistic   
print(f"p-value: {p_val:.4f}") # print the p-value 
print(f"Reject H0 (distributions equal): {p_val < 0.05}") # print the reject H0 (distributions equal): {p_val < 0.05}
