# -------------------------------------------------
# File Name: 09_unpacking.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Tuple Unpacking.
# -------------------------------------------------

print("Example 9: Tuple unpacking")
print("-" * 40)

person = ("John", 25, "Engineer")

# Unpack: one variable per element (must match count)
name, age, profession = person

print("Original tuple:", person)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
