# -------------------------------------------------
# File Name: 16_nested_enumerate.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Use enumerate() for numbered output when iterating dicts.
# -------------------------------------------------

student = {
    "student1": {"name": "John", "age": 25, "major": "Computer Science"},
    "student2": {"name": "Jane", "age": 23, "major": "Mathematics"},
    "student3": {"name": "Jim", "age": 24, "major": "Physics"},
}

print("Enumerate for Numbered Output")
print("-" * 40)
# enumerate(dict) yields (index, key)
for i, key in enumerate(student, start=1):
    print(f"Student {i} ({key}): {student[key]}")
