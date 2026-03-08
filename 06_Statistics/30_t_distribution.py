# -------------------------------------------------
# File Name: 30_t_distribution.py
# Description: Explores Student t distribution probabilities and critical values used in inference.
# -------------------------------------------------

from scipy import stats

df = 10  # degrees of freedom
t_val = 1.5

print("=== T-DISTRIBUTION (df=10) ===")
print(f"P(T <= {t_val}): {stats.t.cdf(t_val, df):.4f}")
print(f"P(T > {t_val}): {1 - stats.t.cdf(t_val, df):.4f}")
print()
# Critical value for 95% CI
t_crit = stats.t.ppf(0.975, df)
print(f"t critical (alpha=0.05, two-tailed): {t_crit:.2f}")
