# -------------------------------------------------
# File Name: 22_tuple_vs_list_performance.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Tuple vs list: memory and speed. sys.getsizeof comparison.
# -------------------------------------------------

import sys

t = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
print("Tuple:", sys.getsizeof(t), "bytes")
print("List:", sys.getsizeof(lst), "bytes")
print("Tuples use less memory (no dynamic resize buffer).")
print("Tuples are faster for iteration and unpacking.")
