# -------------------------------------------------
# File Name: 44_power_of_test.py
# Description: Simulates statistical power as the probability of rejecting H0 when H0 is false.
# -------------------------------------------------

from scipy import stats  # Statistical tests and probability distributions
import numpy as np  # Numerical arrays and vectorized operations

# Power = P(reject H0 | H0 false) = 1 - β
# Depends on: effect size, sample size, alpha
# Simulate power for one-sample t-test
np.random.seed(42)  # Reproducible random results
n_sim = 1000  # Number of Monte Carlo simulations
alpha = 0.05  # Significance level
n = 30 # sample size
true_mean = 105 # true mean
null_mean = 100 # null mean
std = 15 # standard deviation

reject_count = 0  # Number of simulated rejections
for _ in range(n_sim):
    sample = np.random.normal(true_mean, std, n) # Sample
    _, p = stats.ttest_1samp(sample, null_mean) # Test statistic
    if p < alpha:
        reject_count += 1 # Reject count

power = reject_count / n_sim  # Estimated statistical power
print("=== STATISTICAL POWER ===") # Statistical power
print("Power = P(reject H0 | H0 false)") # Power = P(reject H0 | H0 false)
print()
print(f"Setup: H0: mean=100, true mean={true_mean}, n={n}, alpha={alpha}") # print the setup: H0: mean=100, true mean={true_mean}, n={n}, alpha={alpha} 
print(f"Simulated power ({n_sim} runs): {power:.2%}") # print the simulated power ({n_sim} runs): {power:.2%}
print()
print("Larger effect size or n -> higher power") # Larger effect size or n -> higher power
