# -------------------------------------------------
# File Name: 45_margin_of_error.py
# Description: Margen de error.
# -------------------------------------------------

from scipy import stats
import numpy as np

np.random.seed(42)
sample = np.random.normal(100, 15, 100)
n = len(sample)
mean = np.mean(sample)
sem = stats.sem(sample)
alpha = 0.05

# Margin of error = t_crit * SE
t_crit = stats.t.ppf(1 - alpha/2, n - 1)
margin = t_crit * sem
ci_low = mean - margin
ci_high = mean + margin

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
