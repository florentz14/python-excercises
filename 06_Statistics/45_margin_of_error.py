# -------------------------------------------------
# File Name: 45_margin_of_error.py
# Description: Computes margin of error and confidence interval width for a sample mean estimate.
# -------------------------------------------------

from scipy import stats  # Statistical tests and probability distributions
import numpy as np  # Numerical arrays and vectorized operations

np.random.seed(42)  # Reproducible random results
sample = np.random.normal(100, 15, 100) # Sample
n = len(sample)
mean = np.mean(sample)
sem = stats.sem(sample)  # Standard error of the mean
alpha = 0.05  # Significance level

# Margin of error = t_crit * SE
t_crit = stats.t.ppf(1 - alpha/2, n - 1)
margin = t_crit * sem  # Margin of error
ci_low = mean - margin  # Lower confidence bound
ci_high = mean + margin  # Upper confidence bound

print("=== MARGIN OF ERROR ===")
print("MOE = t_critical × (s / √n)")
print()
print(f"Sample mean: {mean:.2f}")
print(f"SE: {sem:.2f}")
print(f"t critical (95%): {t_crit:.2f}")
print(f"Margin of error: ±{margin:.2f}")
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
print()
print("Larger n -> smaller MOE -> narrower CI")
