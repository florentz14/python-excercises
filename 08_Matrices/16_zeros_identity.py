# -------------------------------------------------
# File Name: 16_zeros_identity.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Using list comprehensions without NumPy.
# -------------------------------------------------

zeros = [[0 for _ in range(3)] for _ in range(3)]
print("Zero matrix (3x3):")
for row in zeros:
    print(row)

# Identity matrix 3x3: 1 on diagonal, 0 elsewhere
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("\nIdentity matrix (3x3):")
for row in identity:
    print(row)
