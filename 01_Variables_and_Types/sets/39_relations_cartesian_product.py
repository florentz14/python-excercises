# -------------------------------------------------
# File Name: 39_relations_cartesian_product.py
# Purpose: Relations and Cartesian product
# Description: A relation is a subset of A × B. Introduction to
#              reflexive, symmetric, and transitive properties.
# -------------------------------------------------

from itertools import product

print("Relations and Cartesian Product")
print("-" * 40)

# Cartesian product A × B = {(a,b) | a ∈ A, b ∈ B}
A = {1, 2, 3}
B = {'x', 'y'}

cartesian = set(product(A, B))
print("A =", A, ", B =", B)
print("A × B (Cartesian product):", cartesian)
print("|A × B| =", len(A), "*", len(B), "=", len(cartesian))
print()

# Relation: subset of A × B (e.g., "a is related to b")
# Example: R = {(1,x), (2,y), (3,x)} - a relation from A to B
R = {(1, 'x'), (2, 'y'), (3, 'x')}
print("Relation R (subset of A×B):", R)
print("R ⊆ A×B?", R.issubset(cartesian))
print()

# Reflexive: (a,a) ∈ R for all a ∈ A (relation on A × A)
# Symmetric: (a,b) ∈ R implies (b,a) ∈ R
# Transitive: (a,b),(b,c) ∈ R implies (a,c) ∈ R

# Example: relation on {1,2,3} - "less than"
S = {1, 2, 3}
R_less = {(1, 2), (1, 3), (2, 3)}
print("Relation 'less than' on", S, ":", R_less)
print("Reflexive? (1,1) in R:", (1, 1) in R_less)  # No
print("Symmetric? (1,2) in R, (2,1) in R?", (2, 1) in R_less)  # No
print("Transitive? (1,2),(2,3) in R -> (1,3) in R?", (1, 3) in R_less)  # Yes
