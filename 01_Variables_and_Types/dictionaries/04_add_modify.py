# -------------------------------------------------
# File Name: 04_add_modify.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Add and modify dictionary entries using dict[key] = value.
# -------------------------------------------------

print("Example 4: Add and modify values")
print("-" * 40)

#create a dictionary
car = {"brand": "Toyota", "color": "red"}
print("Original:", car)

#add year
car["year"] = "2023"           # Add new key-value pair (key didn't exist)
print("After adding year:", car)

#modify color
car["color"] = "blue"        # Modify existing value (key already exists)
print("After modifying color:", car)
