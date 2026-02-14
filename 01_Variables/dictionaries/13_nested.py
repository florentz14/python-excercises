# -------------------------------------------------
# File Name: 13_nested.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Nested Dictionaries.
#              A dictionary can contain other dictionaries as
#              values, creating a hierarchical data structure.
#              Access nested values by chaining keys:
#              dict["outer"]["inner"].
# -------------------------------------------------

# Example 13: Dictionary with nested structures
print("Example 13: Dictionary with nested structures")
print("-" * 40)

# student dictionary
student = {
    "student1": {
        "name": "John",
        "age": 25,
        "major": "Computer Science",
        "gpa": 3.8,
        "student_id": "CS2024001",
        "major": "Computer Science",
    },
    "student2": {
        "name": "Jane",
        "age": 23,
        "major": "Mathematics",
        "gpa": 3.5,
        "student_id": "CS2024002",
        "major": "Mathematics",
    },
    "student3": {
        "name": "Jim",
        "age": 24,
        "major": "Physics",
        "gpa": 3.7,
        "student_id": "CS2024003",
        "major": "Physics",
    }
}
print("Student dictionary:", student)
print("-" * 60)

# Chain keys to reach nested values
print("Student 1 name:", student["student1"]["name"])   # Access inner dict value
print("Student 2 age:", student["student2"]["age"])
print("Student 3 age:", student["student3"]["age"])

# Chain keys to reach nested values
print("Student 1 major:", student["student1"]["major"])   # Access inner dict value
print("Student 2 gpa:", student["student2"]["gpa"])
print("Student 3 gpa:", student["student3"]["gpa"])

# Chain keys to reach nested values
print("Student 1 student_id:", student["student1"]["student_id"])   # Access inner dict value
print("Student 2 student_id:", student["student2"]["student_id"])
print("Student 3 student_id:", student["student3"]["student_id"])
print("-" * 60)

# loop through the dictionary and print the only the keys
print("Loop through the dictionary and print the only the keys")
for key in student.keys():
    print(f"Key: {key}")
print("-" * 60)

# loop through the dictionary and print the only the values
print("Loop through the dictionary and print the only the values")
for value in student.values():
    print(f"Value: {value}")
print("-" * 60)

# loop through the dictionary and print the key and value
print("Loop through the dictionary and print the key and value")
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
print("-" * 60)

# Iterate over each student record using enumerate for numbering
# enumerate(dict) yields (index, key); use student[key] to get the nested record
print("Iterate over each student record using enumerate for numbering")
for i, key in enumerate(student, start=1):
    print(f"Student {i} ({key}): {student[key]}")
print("-" * 60)

# All dictionary keys as a list
print("All dictionary keys as a list")
print(list(student.keys()))
print("-" * 60)

# All dictionary values as a list
print("All dictionary values as a list")
print(list(student.values()))
print("-" * 60)

# All dictionary keys and values as a list  (list of tuples)
print("All dictionary keys and values as a list  (list of tuples)")
print(list(student.items()))
print("-" * 60)
