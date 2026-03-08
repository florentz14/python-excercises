# -------------------------------------------------
# File Name: 30_t_distribution.py
# Description: Explores Student t distribution probabilities and critical values used in inference.
# -------------------------------------------------

from scipy import stats  # Statistical tests and probability distributions

df = 10  # degrees of freedom
t_val = 1.5 # t-value

print("=== T-DISTRIBUTION (df=10) ===")
print(f"P(T <= {t_val}): {stats.t.cdf(t_val, df):.4f}") # print the probability of T <= t_val
print(f"P(T > {t_val}): {1 - stats.t.cdf(t_val, df):.4f}") # print the probability of T > t_val
print()
# Critical value for 95% CI
t_crit = stats.t.ppf(0.975, df) # Critical value for 95% CI
print(f"t critical (alpha=0.05, two-tailed): {t_crit:.2f}")
