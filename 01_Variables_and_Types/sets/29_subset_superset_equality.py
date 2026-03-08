# -------------------------------------------------
# File Name: 29_subset_superset_equality.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Demonstrates subset (<=), proper subset (<), superset (>=),
# -------------------------------------------------

print("Subset, Proper Subset, Superset, and Equality")
print("-" * 40)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

print("A =", A, ", B =", B, ", C =", C)
print()

# A <= B: subset (all elements of A are in B)
print("A <= B (subset):", A <= B)  # True

# A < B: proper subset (A is subset of B but A != B)
print("A < B (proper subset):", A < B)  # True

# B >= A: superset (B contains all elements of A)
print("B >= A (superset):", B >= A)  # True

# A == C: equality (same elements)
print("A == C (equality):", A == C)  # True

# A < C: proper subset when equal? No (A == C, so not proper)
print("A < C (proper subset when equal):", A < C)  # False

# B <= A: B is not a subset of A
print("B <= A (B subset of A?):", B <= A)  # False
