# Example 5: Remove items from dictionary
print("Example 5: Remove items from dictionary")
print("-" * 40)
inventory = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
print("Original:", inventory)
removed = inventory.pop("banana")  # Remove and return value
print(f"Removed banana: {removed}")
print("After pop:", inventory)
del inventory["grape"]  # Delete an item
print("After del grape:", inventory)
