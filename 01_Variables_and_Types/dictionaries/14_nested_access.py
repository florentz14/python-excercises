# -------------------------------------------------
# File Name: 14_nested_access.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Access nested values by chaining keys: dict["outer"]["inner"].
# -------------------------------------------------

student = {
    "student1": {"name": "John", "age": 25, "major": "Computer Science", "gpa": 3.8},
    "student2": {"name": "Jane", "age": 23, "major": "Mathematics", "gpa": 3.5},
    "student3": {"name": "Jim", "age": 24, "major": "Physics", "gpa": 3.7},
}

print("Accessing Nested Values (Key Chaining)")
print("-" * 40)
# Chain keys to reach nested values
print("Student 1 name:", student["student1"]["name"])
print("Student 2 age:", student["student2"]["age"])
print("Student 3 gpa:", student["student3"]["gpa"])
print("Student 1 major:", student["student1"]["major"])
