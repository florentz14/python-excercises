# -------------------------------------------------
# File Name: 08_concatenation_repetition.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Tuple Concatenation and Repetition.
# -------------------------------------------------

print("Example 8: Tuple concatenation and repetition")
print("-" * 40)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# + creates a new tuple by joining two tuples
combined = tuple1 + tuple2
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Combined (tuple1 + tuple2):", combined)   # (1, 2, 3, 4, 5, 6)

# * repeats the tuple a given number of times
repeated = tuple1 * 3
print("Repeated (tuple1 * 3):", repeated)        # (1, 2, 3, 1, 2, 3, 1, 2, 3)
