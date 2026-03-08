# -------------------------------------------------
# File Name: 32_update_operations.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: In-place set update methods: update(), intersection_update(),
# -------------------------------------------------

print("Set Update Operations (In-Place)")
print("-" * 40)

# update(): add all elements from iterable (union in place)
s = {1, 2, 3}
s.update([3, 4, 5])
print("update([3,4,5]):", s)  # {1, 2, 3, 4, 5}
print()

# intersection_update(): keep only elements in both
s = {1, 2, 3, 4}
s.intersection_update({2, 3, 5, 6})
print("intersection_update({2,3,5,6}):", s)  # {2, 3}
print()

# difference_update(): remove elements that are in other
s = {1, 2, 3, 4}
s.difference_update({2, 4})
print("difference_update({2,4}):", s)  # {1, 3}
print()

# symmetric_difference_update(): replace with A ^ B
s = {1, 2, 3}
s.symmetric_difference_update({2, 3, 4})
print("symmetric_difference_update({2,3,4}):", s)  # {1, 4}

# Shorthand operators: |=, &=, -=, ^=
a = {1, 2}
a |= {2, 3}  # same as update
print("a |= {2,3}:", a)
