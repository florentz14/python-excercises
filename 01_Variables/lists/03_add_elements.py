# -------------------------------------------------
# File Name: 03_add_elements.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Add Elements to a List.
#              append() adds a single item at the end.
#              extend() adds all items from an iterable.
#              insert(i, x) places x at position i.
# -------------------------------------------------

print("Example 3: Add elements to a list")
print("-" * 40)

colors = ["red", "blue"]
print("Original list:", colors)

colors.append("green")                    # Add one element at the end
print("After append:", colors)

colors.extend(["yellow", "purple"])       # Add multiple elements from a list
print("After extend:", colors)
