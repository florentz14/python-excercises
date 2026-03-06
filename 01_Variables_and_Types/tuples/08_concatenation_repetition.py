# -------------------------------------------------
# File Name: 08_concatenation_repetition.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Tuple Concatenation and Repetition.
#              The + operator joins two tuples into a new one.
#              The * operator repeats a tuple n times. Both
#              produce new tuples (originals stay unchanged).
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
