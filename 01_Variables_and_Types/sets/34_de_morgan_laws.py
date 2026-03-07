# -------------------------------------------------
# File Name: 34_de_morgan_laws.py
# Purpose: Verify De Morgan's laws for sets
# Description: (A ∪ B)' = A' ∩ B'  and  (A ∩ B)' = A' ∪ B'
#              Using complement relative to universal set U.
# -------------------------------------------------

print("De Morgan's Laws Verification")
print("-" * 40)

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # universal set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Complement: A' = U - A
def complement(s, universe):
    return universe - s

A_complement = complement(A, U)
B_complement = complement(B, U)

print("U =", U)
print("A =", A, "  A' =", A_complement)
print("B =", B, "  B' =", B_complement)
print()

# Law 1: (A ∪ B)' = A' ∩ B'
left1 = complement(A | B, U)
right1 = A_complement & B_complement
print("(A ∪ B)' =", left1)
print("A' ∩ B' =", right1)
print("(A ∪ B)' = A' ∩ B'?", left1 == right1)
print()

# Law 2: (A ∩ B)' = A' ∪ B'
left2 = complement(A & B, U)
right2 = A_complement | B_complement
print("(A ∩ B)' =", left2)
print("A' ∪ B' =", right2)
print("(A ∩ B)' = A' ∪ B'?", left2 == right2)
