# -------------------------------------------------
# File Name: 11_immutability.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Tuple Immutability.
#              Tuples cannot be modified after creation.
#              Attempting to assign to an index raises
#              TypeError. This immutability makes tuples
#              hashable (usable as dict keys or set elements).
# -------------------------------------------------

print("Example 11: Tuple immutability")
print("-" * 40)

my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# Trying to change an element raises TypeError
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: Tuples are immutable! - {e}")
