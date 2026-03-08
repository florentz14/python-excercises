# -------------------------------------------------
# File Name: 05_remove.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Remove items with pop() (returns value) or del (no return).
# -------------------------------------------------

print("Example 5: Remove items from dictionary")
print("-" * 40)

# Create a dictionary
inventory = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
print("Original:", inventory)

# Remove banana
removed = inventory.pop("banana")   # Remove key and return its value
print(f"Removed banana: {removed}")
print("After pop:", inventory)

# Remove grape
del inventory["grape"]              # Delete key without returning value
print("After del grape:", inventory)
