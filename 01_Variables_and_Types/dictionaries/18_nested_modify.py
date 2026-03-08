# -------------------------------------------------
# File Name: 18_nested_modify.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Update, add, or delete keys in nested dictionaries.
# -------------------------------------------------

student = {
    "student1": {"name": "John", "age": 25, "gpa": 3.8},
    "student2": {"name": "Jane", "age": 23, "gpa": 3.5},
}

print("Modifying Nested Values")
print("-" * 40)

# Update existing nested value
student["student1"]["gpa"] = 3.9
print("After updating student1 gpa:", student["student1"]["gpa"])

# Add new key to nested dict
student["student1"]["major"] = "Computer Science"
print("After adding major:", student["student1"])

# Delete key from nested dict
del student["student2"]["gpa"]
print("After deleting student2 gpa:", student["student2"])
