# -------------------------------------------------
# File Name: 14_convert_list_tuple.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Convert Between List and Tuple.
#              tuple(list) converts a list to a tuple.
#              list(tuple) converts a tuple back to a list.
#              Useful when you need mutability temporarily.
# -------------------------------------------------

print("Example 14: Convert list to tuple and vice versa")
print("-" * 40)

list_data = [10, 20, 30, 40]

# Convert list -> tuple (now immutable)
tuple_data = tuple(list_data)
print("Original list:", list_data)
print("Converted to tuple:", tuple_data)

# Convert tuple -> list (now mutable again)
back_to_list = list(tuple_data)
print("Converted back to list:", back_to_list)
