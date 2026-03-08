# -------------------------------------------------
# File Name: 35_bayes_theorem.py
# Description: Applies Bayes theorem to compute posterior probability from prevalence and test characteristics.
# -------------------------------------------------

# P(A|B) = P(B|A) * P(A) / P(B)
# Example: disease given positive test
p_disease = 0.01       # prevalence (P(A))
p_pos_given_disease = 0.95   # sensitivity (P(B|A))
p_pos_given_no_disease = 0.05  # false positive rate (P(B|¬A))

p_no_disease = 1 - p_disease  # Complement probability (P(¬A))
p_pos = p_pos_given_disease * p_disease + p_pos_given_no_disease * p_no_disease  # Total probability of a positive test
p_disease_given_pos = p_pos_given_disease * p_disease / p_pos  # Posterior probability (P(A|B))

print("=== BAYES' THEOREM ===")
print("P(A|B) = P(B|A) * P(A) / P(B)") # P(A|B) = P(B|A) * P(A) / P(B)
print()
print("Example: P(disease | positive test)") # Example: P(disease | positive test)
print(f"  P(disease) = {p_disease}")
print(f"  P(positive | disease) = {p_pos_given_disease}") # print the probability of a positive test given the disease
print(f"  P(positive | no disease) = {p_pos_given_no_disease}") # print the probability of a positive test given no disease
print(f"  P(positive) = {p_pos:.4f}")
print(f"  P(disease | positive) = {p_disease_given_pos:.4f}")
