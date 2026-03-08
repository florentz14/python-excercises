# -------------------------------------------------
# File Name: 03_add_elements.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Add Elements to a List.
# -------------------------------------------------

print("Example 3: Add elements to a list")
print("-" * 40)

colors = ["red", "blue"]
print("Original list:", colors)

colors.append("green")                    # Add one element at the end
print("After append:", colors)

colors.extend(["yellow", "purple"])       # Add multiple elements from a list
print("After extend:", colors)
