# -------------------------------------------------
# File Name: 31_chi_square_distribution.py
# Description: Explores chi-square distribution probabilities and critical values.
# -------------------------------------------------

from scipy import stats  # Statistical tests and probability distributions

df = 5 # degrees of freedom
x_val = 8 # x-value

print("=== CHI-SQUARE (df=5) ===")
print(f"P(X <= {x_val}): {stats.chi2.cdf(x_val, df):.4f}") # print the probability of X <= x_val
print(f"Mean = df: {df}, Variance = 2*df: {2*df}") # print the mean = df, variance = 2*df
print()
# Critical value for chi-square test
chi_crit = stats.chi2.ppf(0.95, df) # Critical value for chi-square test
print(f"chi2 critical (alpha=0.05, df=5): {chi_crit:.2f}") # print the critical value for chi-square test
