# -------------------------------------------------
# File Name: 13_nested.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Nested Tuples.
# -------------------------------------------------

print("Example 13: Nested tuples")
print("-" * 40)

# Each element of the outer tuple is itself a tuple
nested = ((1, 2), ("a", "b"), (True, False))
print("Nested tuple:", nested)

print("First inner tuple:", nested[0])                   # (1, 2)
print("First element of first inner tuple:", nested[0][0])  # 1
