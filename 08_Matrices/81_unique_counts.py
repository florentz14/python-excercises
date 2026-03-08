# -------------------------------------------------
# File Name: 81_unique_counts.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: unique, return_counts, bincount for non-negative ints.
# -------------------------------------------------

import numpy as np

v = np.array([3, 1, 2, 3, 2, 1, 3])
print("Array:", v)

# Unique values (sorted)
u = np.unique(v)
print("np.unique:", u)

# Unique with counts
u, counts = np.unique(v, return_counts=True)
print("Unique:", u)
print("Counts:", counts)
for val, cnt in zip(u, counts):
    print(f"  {val}: {cnt}")

# bincount: for non-negative integers, count occurrences of 0,1,2,...
b = np.bincount(v)  # index i = count of value i
print("\nbincount:", b)
print("  (count of 0:", b[0], ", count of 1:", b[1], ", ...)")

# argmax of bincount = most frequent
most_freq = np.argmax(np.bincount(v))
print("Most frequent value:", most_freq)
