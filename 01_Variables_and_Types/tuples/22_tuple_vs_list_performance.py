# ------------------------------------------------------------
# File: 22_tuple_vs_list_performance.py
# Purpose: Tuple vs list: memory and speed.
# Description: sys.getsizeof, basic timeit comparison.
# ------------------------------------------------------------

import sys

t = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
print("Tuple:", sys.getsizeof(t), "bytes")
print("List:", sys.getsizeof(lst), "bytes")
print("Tuples use less memory (no dynamic resize buffer).")
print("Tuples are faster for iteration and unpacking.")
