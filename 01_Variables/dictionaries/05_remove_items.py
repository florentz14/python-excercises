# -------------------------------------------------
# File Name: 05_remove_items.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Remove Items from a Dictionary.
#              pop(key) removes a key and returns its value.
#              del dict[key] removes a key without returning.
#              Both raise KeyError if the key does not exist.
# -------------------------------------------------

# Example 5: Remove items from dictionary
print("Example 5: Remove items from dictionary")
print("-" * 40)

inventory = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
print("Original:", inventory)

removed = inventory.pop("banana")   # Remove key and return its value
print(f"Removed banana: {removed}")
print("After pop:", inventory)

del inventory["grape"]              # Delete key without returning value
print("After del grape:", inventory)
