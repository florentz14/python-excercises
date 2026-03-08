# -------------------------------------------------
# File Name: 04_remove_elements.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Remove Elements from a List.
# -------------------------------------------------

print("Example 4: Remove elements from a list")
print("-" * 40)

animals = ["cat", "dog", "bird", "fish", "dog"]
print("Original list:", animals)

animals.remove("dog")                     # Remove first occurrence of "dog"
print("After remove 'dog':", animals)

removed_item = animals.pop()              # Remove and return the last element
print("Popped item:", removed_item)
print("After pop:", animals)
