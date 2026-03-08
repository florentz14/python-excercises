# -------------------------------------------------
# File Name: 28_comp_enumerate.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Use enumerate() in comprehension for index-to-item mappings.
# -------------------------------------------------

print("9. Using enumerate() in Comprehension:")
print("-" * 60)
fruits = ["apple", "banana", "cherry", "date"]
# Swap order: fruit as key, index as value (enumerate returns index first)
fruit_index = {fruit: index for index, fruit in enumerate(fruits)}
print(f"Fruit indices: {fruit_index}")
