# -------------------------------------------------
# File Name: 44_power_of_test.py
# Description: Potencia estadística.
# -------------------------------------------------

from scipy import stats
import numpy as np

# Power = P(reject H0 | H0 false) = 1 - β
# Depends on: effect size, sample size, alpha
# Simulate power for one-sample t-test
np.random.seed(42)
n_sim = 1000
alpha = 0.05
n = 30
true_mean = 105  # H0: mean=100 is false
null_mean = 100
std = 15

reject_count = 0
for _ in range(n_sim):
    sample = np.random.normal(true_mean, std, n)
    _, p = stats.ttest_1samp(sample, null_mean)
    if p < alpha:
        reject_count += 1

power = reject_count / n_sim
print("=== STATISTICAL POWER ===")
print("Power = P(reject H0 | H0 false)")
print()
print(f"Setup: H0: mean=100, true mean={true_mean}, n={n}, alpha={alpha}")
print(f"Simulated power ({n_sim} runs): {power:.2%}")
print()
print("Larger effect size or n -> higher power")
