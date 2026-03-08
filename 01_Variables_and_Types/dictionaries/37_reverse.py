# -------------------------------------------------
# File Name: 37_reverse.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Reverse/invert key-value pairs. Handles duplicates with lists.
# -------------------------------------------------

from collections import defaultdict
original = {'a': 1, 'b': 2, 'c': 3}
print("Original:", original)

# Simple reverse (assuming unique values)
reversed_dict = {value: key for key, value in original.items()}
print("Reversed:", reversed_dict)

# Handling duplicate values - collect keys in list

original_dup = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print("Original with duplicates:", original_dup)

reversed_dup = defaultdict(list)
for key, value in original_dup.items():
    reversed_dup[value].append(key)

print("Reversed with lists:", dict(reversed_dup))

# Using dict comprehension with lists
reversed_lists = {}
for key, value in original_dup.items():
    reversed_lists.setdefault(value, []).append(key)
print("Reversed with setdefault:", reversed_lists)
