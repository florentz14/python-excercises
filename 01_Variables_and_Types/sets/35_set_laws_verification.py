# -------------------------------------------------
# File Name: 35_set_laws_verification.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Verify fundamental set laws: commutative, associative,
# -------------------------------------------------

print("Set Laws Verification")
print("-" * 40)

A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
U = {1, 2, 3, 4, 5, 6}
empty = set()

# Commutative: A ∪ B = B ∪ A, A ∩ B = B ∩ A
print("Commutative:")
print("  A | B == B | A:", (A | B) == (B | A))
print("  A & B == B & A:", (A & B) == (B & A))
print()

# Associative: (A ∪ B) ∪ C = A ∪ (B ∪ C)
print("Associative:")
print("  (A|B)|C == A|(B|C):", ((A | B) | C) == (A | (B | C)))
print("  (A&B)&C == A&(B&C):", ((A & B) & C) == (A & (B & C)))
print()

# Distributive: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
print("Distributive:")
left = A | (B & C)
right = (A | B) & (A | C)
print("  A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C):", left == right)
left2 = A & (B | C)
right2 = (A & B) | (A & C)
print("  A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C):", left2 == right2)
print()

# Identity: A ∪ ∅ = A, A ∩ U = A (with U as universe)
print("Identity:")
print("  A | ∅ == A:", (A | empty) == A)
print("  A ∩ U == A (U superset):", (A & U) == A)
print()

# Idempotent: A ∪ A = A, A ∩ A = A
print("Idempotent:")
print("  A | A == A:", (A | A) == A)
print("  A & A == A:", (A & A) == A)
