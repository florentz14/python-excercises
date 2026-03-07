# -------------------------------------------------
# File Name: 30_symmetric_difference.py
# Purpose: Symmetric difference (A ^ B)
# Description: Elements in one set or the other but not both.
#              Equivalent to (A - B) | (B - A) or (A | B) - (A & B).
# -------------------------------------------------

print("Symmetric Difference (A ^ B)")
print("-" * 40)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A =", A)
print("B =", B)
print()

# A ^ B: elements in A or B but not in both
sym_diff = A ^ B
print("A ^ B (symmetric_difference):", sym_diff)
print("  Elements in A only:", A - B)
print("  Elements in B only:", B - A)
print("  Union of both = A ^ B:", (A - B) | (B - A))

# Using method
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# Verify: (A | B) - (A & B) = A ^ B
union_minus_intersection = (A | B) - (A & B)
print("(A | B) - (A & B) equals A ^ B:", union_minus_intersection == sym_diff)
