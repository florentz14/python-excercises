# -------------------------------------------------
# File Name: 21_copy_vs_deepcopy.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Demonstrates shallow copy vs deep copy.
# -------------------------------------------------

import copy

# Shallow copy
original = [1, [2, 3], 4]
shallow = copy.copy(original)
shallow[1][0] = 'changed'

print("Original after shallow copy modification:", original)
print("Shallow copy:", shallow)

# Deep copy
original2 = [1, [2, 3], 4]
deep = copy.deepcopy(original2)
deep[1][0] = 'changed'

print("Original after deep copy modification:", original2)
print("Deep copy:", deep)