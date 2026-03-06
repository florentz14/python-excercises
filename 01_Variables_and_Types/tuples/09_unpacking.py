# -------------------------------------------------
# File Name: 09_unpacking.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Tuple Unpacking.
#              Assign each element of a tuple to individual
#              variables in a single statement. The number of
#              variables must match the number of elements.
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
