# -------------------------------------------------
# File Name: 20_one_sample_ttest.py
# Author: Florentino Báez
# Description: Runs a one-sample t-test to compare a sample mean against a reference population mean.
# -------------------------------------------------

import numpy as np # Fast numerical operations
from scipy import stats # Statistical tests

np.random.seed(42) # Seed for reproducibility
group_a = np.random.normal(100, 15, 30) # Group A

print("=== GROUP ===")
print(f"Mean: {np.mean(group_a):.2f}, Std: {np.std(group_a, ddof=1):.2f}") # Mean and standard deviation of Group A
print()

# One-sample t-test (H0: mean = 100)
t_stat, p_value = stats.ttest_1samp(group_a, 100) # One-sample t-test (H0: mean = 100)  (H0: mean = 100)    (H0: mean = 100)    
print("=== ONE-SAMPLE T-TEST (H0: mean=100) ===") # One-sample t-test (H0: mean=100)
print(f"t-statistic: {t_stat:.4f}") # t-statistic
print(f"p-value: {p_value:.4f}") # p-value
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}") # Reject H0 at alpha=0.05 (H0: mean = 100)
