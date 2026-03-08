# -------------------------------------------------
# File Name: 13_nested_basic.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Basic nested dictionary structure with dicts as values.
# -------------------------------------------------

print("Basic Nested Dictionary Structure")
print("-" * 40)

student = {
    "student1": {
        "name": "John",
        "age": 25,
        "major": "Computer Science",
        "gpa": 3.8,
        "student_id": "CS2024001",
    },
    "student2": {
        "name": "Jane",
        "age": 23,
        "major": "Mathematics",
        "gpa": 3.5,
        "student_id": "CS2024002",
    },
    "student3": {
        "name": "Jim",
        "age": 24,
        "major": "Physics",
        "gpa": 3.7,
        "student_id": "CS2024003",
    }
}
print("Student dictionary:", student)
