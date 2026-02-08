# -------------------------------------------------
# File Name: 19_anidadas_copiar.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Nested Lists and Copying (Shallow vs Deep).
#              A matrix is a list of lists. copy() creates
#              a shallow copy (inner lists are shared).
#              copy.deepcopy() creates a fully independent
#              copy so changes don't propagate.
# -------------------------------------------------

import copy

print("=== Nested lists (matrix) ===")
# A 3x3 matrix represented as a list of lists
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("3x3 Matrix:")
for fila in matriz:
    print(f"  {fila}")
print(f"Element [1][2]: {matriz[1][2]}\n")   # Row 1, Column 2 -> 6

print("=== Copying lists ===")
original = [1, 2, 3, [4, 5]]

# Shallow copy: inner list is still shared (same reference)
copia_superficial = original.copy()

# Deep copy: completely independent, inner list is duplicated
copia_profunda = copy.deepcopy(original)

# Modify the nested list inside the original
original[3].append(6)

print(f"Original:                          {original}")
print(f"Shallow copy (affected by change): {copia_superficial}")
print(f"Deep copy (not affected):          {copia_profunda}")
