# -------------------------------------------------
# File Name: 11_binomial_distribution.py
# Author: Florentino Báez
# Description: Computes binomial PMF/CDF values and prints probabilities across possible success counts.
# -------------------------------------------------

from scipy import stats

n, p = 10, 0.5

print("=== BINOMIAL (n=10, p=0.5) ===")
print(f"P(k=5): {stats.binom.pmf(5, n, p):.4f}")
print(f"P(k <= 5): {stats.binom.cdf(5, n, p):.4f}")

binom_probs = [stats.binom.pmf(k, n, p) for k in range(n + 1)]
print(f"PMF for k=0..10: {[round(x, 3) for x in binom_probs]}")
