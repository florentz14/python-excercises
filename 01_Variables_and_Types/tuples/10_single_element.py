# -------------------------------------------------
# File Name: 10_single_element.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Single-Element Tuple.
# -------------------------------------------------

print("Example 10: Single element tuple")
print("-" * 40)

single = (42,)            # Trailing comma makes it a tuple
print("Single element tuple:", single)
print("Type:", type(single))           # <class 'tuple'>

not_tuple = (42)          # No comma — this is just an int
print("Without comma:", not_tuple)
print("Type:", type(not_tuple))        # <class 'int'>
