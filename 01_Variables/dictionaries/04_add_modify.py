# -------------------------------------------------
# File Name: 04_add_modify.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Add and Modify Dictionary Values.
#              Assigning to a new key adds a new entry.
#              Assigning to an existing key overwrites
#              the previous value. Both use dict[key] = value.
# -------------------------------------------------

# Example 4: Add and modify values
print("Example 4: Add and modify values")
print("-" * 40)

car = {"brand": "Toyota", "color": "red"}
print("Original:", car)

car["year"] = 2023           # Add new key-value pair (key didn't exist)
print("After adding year:", car)

car["color"] = "blue"        # Modify existing value (key already exists)
print("After modifying color:", car)
