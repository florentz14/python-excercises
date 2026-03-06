# -------------------------------------------------
# File Name: 10_single_element.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Single-Element Tuple.
#              A trailing comma is required to create a
#              one-element tuple: (42,). Without the comma,
#              (42) is just an integer in parentheses.
# -------------------------------------------------

print("Example 10: Single element tuple")
print("-" * 40)

single = (42,)            # Trailing comma makes it a tuple
print("Single element tuple:", single)
print("Type:", type(single))           # <class 'tuple'>

not_tuple = (42)          # No comma — this is just an int
print("Without comma:", not_tuple)
print("Type:", type(not_tuple))        # <class 'int'>
