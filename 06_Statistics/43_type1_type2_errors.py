# -------------------------------------------------
# File Name: 43_type1_type2_errors.py
# Description: Summarizes Type I/Type II errors and their relationship with alpha, beta, and statistical power.
# -------------------------------------------------

print("=== TYPE I AND TYPE II ERRORS ===")
print()
print("               H0 true          H0 false") # H0 true          H0 false
print("Reject H0      Type I (α)      Correct (1-β, power)") # Reject H0      Type I (α)      Correct (1-β, power)
print("Fail to reject Correct         Type II (β)") # Fail to reject Correct         Type II (β)
print()
print("Type I (α): Reject H0 when H0 is true. False positive.") # Type I (α): Reject H0 when H0 is true. False positive.
print("  Controlled by alpha (e.g. 0.05)") # Controlled by alpha (e.g. 0.05)
print()
print("Type II (β): Fail to reject H0 when H0 is false. False negative.") # Type II (β): Fail to reject H0 when H0 is false. False negative.
print("  Power = 1 - β = P(reject H0 | H0 false)") # Power = 1 - β = P(reject H0 | H0 false)
print()
print("Trade-off: Lower α -> higher β (less power)") # Trade-off: Lower α -> higher β (less power)
