# -------------------------------------------------
# File Name: 46_chi_square_test.py
# Description: Prueba chi-cuadrado de independencia.
# -------------------------------------------------

import numpy as np
from scipy import stats

# Contingency table: rows=gender, cols=preference
observed = np.array([
    [30, 20, 10],
    [15, 25, 20],
])

chi2, p_val, dof, expected = stats.chi2_contingency(observed)

print("=== CHI-SQUARE TEST (independence) ===")
print("Observed:")
print(observed)
print()
print("Expected (under H0: independence):")
print(expected)
print()
print(f"chi2 = {chi2:.2f}")
print(f"df = {dof}")
print(f"p-value = {p_val:.4f}")
print(f"Reject H0 (independence): {p_val < 0.05}")
