# -------------------------------------------------
# File Name: 15_nested_iterate.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Iterate over nested dicts with keys(), values(), items().
# -------------------------------------------------

student = {
    "student1": {"name": "John", "age": 25, "major": "Computer Science"},
    "student2": {"name": "Jane", "age": 23, "major": "Mathematics"},
    "student3": {"name": "Jim", "age": 24, "major": "Physics"},
}

print("Iterating Nested Dictionary")
print("-" * 40)

# Loop through keys only
print("Keys:")
for key in student.keys():
    print(f"  {key}")

# Loop through values only (each value is a nested dict)
print("\nValues (nested dicts):")
for value in student.values():
    print(f"  {value}")

# Loop through key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")
