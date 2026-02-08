# -------------------------------------------------
# File Name: 10_min_max_pop.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Find Min/Max and Pop Elements.
#              min() and max() return the smallest and largest
#              elements. pop() removes and returns an arbitrary
#              element (since sets are unordered, you cannot
#              predict which one).
# -------------------------------------------------

# Example 15: Find and remove elements
print("Example 15: Find and remove elements")
print("-" * 40)

num_set = {50, 10, 40, 20, 30}
print("Original set:", num_set)

print("Max element:", max(num_set))     # 50 — largest value
print("Min element:", min(num_set))     # 10 — smallest value

popped = num_set.pop()                  # Remove and return an arbitrary element
print(f"Popped element: {popped}")
print("After pop:", num_set)
