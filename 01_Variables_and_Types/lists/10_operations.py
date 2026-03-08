# -------------------------------------------------
# File Name: 10_operations.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: List Concatenation and Repetition.
# -------------------------------------------------

print("Example 10: List operations")
print("-" * 40)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# + creates a new list by joining two lists
combined = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Combined (list1 + list2):", combined)   # [1, 2, 3, 4, 5, 6]

# * repeats the list a given number of times
repeated = list1 * 3
print("Repeated (list1 * 3):", repeated)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
