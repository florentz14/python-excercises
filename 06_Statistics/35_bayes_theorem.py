# -------------------------------------------------
# File Name: 35_bayes_theorem.py
# Description: Teorema de Bayes.
# -------------------------------------------------

# P(A|B) = P(B|A) * P(A) / P(B)
# Example: disease given positive test
p_disease = 0.01       # prevalence
p_pos_given_disease = 0.95   # sensitivity
p_pos_given_no_disease = 0.05  # false positive rate

p_no_disease = 1 - p_disease
p_pos = p_pos_given_disease * p_disease + p_pos_given_no_disease * p_no_disease
p_disease_given_pos = p_pos_given_disease * p_disease / p_pos

print("=== BAYES' THEOREM ===")
print("P(A|B) = P(B|A) * P(A) / P(B)")
print()
print("Example: P(disease | positive test)")
print(f"  P(disease) = {p_disease}")
print(f"  P(positive | disease) = {p_pos_given_disease}")
print(f"  P(positive | no disease) = {p_pos_given_no_disease}")
print(f"  P(positive) = {p_pos:.4f}")
print(f"  P(disease | positive) = {p_disease_given_pos:.4f}")
