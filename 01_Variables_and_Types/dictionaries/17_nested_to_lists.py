# -------------------------------------------------
# File Name: 17_nested_to_lists.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Convert dict views to lists with list(keys/values/items).
# -------------------------------------------------

student = {
    "student1": {"name": "John", "age": 25},
    "student2": {"name": "Jane", "age": 23},
    "student3": {"name": "Jim", "age": 24},
}

print("Dictionary Views to Lists")
print("-" * 40)

# All keys as list
print("Keys as list:", list(student.keys()))

# All values as list (nested dicts)
print("Values as list:", list(student.values()))

# All key-value pairs as list of tuples
print("Items as list (tuples):", list(student.items()))
