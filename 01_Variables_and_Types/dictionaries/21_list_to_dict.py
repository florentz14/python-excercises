# -------------------------------------------------
# File Name: 21_list_to_dict.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Convert list of (key, value) tuples to dict with dict().
# -------------------------------------------------

print("Example 15: Convert list of tuples to dictionary")
print("-" * 40)

# Each tuple is a (key, value) pair
pairs = [("name", "Alice"), ("age", 30), ("city", "Boston")]

# dict() converts the list of tuples into a dictionary
person_dict = dict(pairs)

print("List of tuples:", pairs)
print("Converted to dictionary:", person_dict)
