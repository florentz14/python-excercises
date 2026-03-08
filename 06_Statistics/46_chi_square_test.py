# -------------------------------------------------
# File Name: 46_chi_square_test.py
# Description: Runs chi-square test of independence on a contingency table.
# -------------------------------------------------

import numpy as np  # Numerical arrays and vectorized operations
from scipy import stats  # Statistical tests and probability distributions

# Contingency table: rows=gender, cols=preference
observed = np.array([
    [30, 20, 10],
    [15, 25, 20],
])

chi2, p_val, dof, expected = stats.chi2_contingency(observed)  # Chi-square statistic

print("=== CHI-SQUARE TEST (independence) ===")
print("Observed:") # Observed:  
print(observed) # print the observed
print()
print("Expected (under H0: independence):") # Expected (under H0: independence):
print(expected) # print the expected
print()
print(f"chi2 = {chi2:.2f}") # print the chi2
print(f"df = {dof}") # print the df
print(f"p-value = {p_val:.4f}") # print the p-value 
print(f"Reject H0 (independence): {p_val < 0.05}") # print the reject H0 (independence): {p_val < 0.05}
