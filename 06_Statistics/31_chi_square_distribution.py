# -------------------------------------------------
# File Name: 31_chi_square_distribution.py
# Description: Explores chi-square distribution probabilities and critical values.
# -------------------------------------------------

from scipy import stats

df = 5
x_val = 8

print("=== CHI-SQUARE (df=5) ===")
print(f"P(X <= {x_val}): {stats.chi2.cdf(x_val, df):.4f}")
print(f"Mean = df: {df}, Variance = 2*df: {2*df}")
print()
# Critical value for chi-square test
chi_crit = stats.chi2.ppf(0.95, df)
print(f"chi2 critical (alpha=0.05, df=5): {chi_crit:.2f}")
