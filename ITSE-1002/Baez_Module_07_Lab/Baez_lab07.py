# -------------------------------------------------
# File Name: Baez_lab07.py
# Author: Florentino Baez
# professor: Mauricio Quiroga
# course: ITSE-1002: Python Programming
# module: 07
# lab: 07 — Student Management System
# date: 2026-02-24
# description: Student Management System using nested dictionaries
#              and sets. Part 1: Dictionaries. Part 2: Sets.
#              No user input or menus required. 
# -------------------------------------------------

# =====================================================
# PART 1 — STUDENT DATABASE USING DICTIONARIES 
# =====================================================

# -------------------------------------------------
# Step 1 — Create the Data (Required)
# Nested dictionary with at least 4 students.
# Each student: name, age, major, gpa
# -------------------------------------------------
students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "major": "CS",
        "gpa": 3.8,
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "major": "Math",
        "gpa": 3.4,
    },
    "S003": {
        "name": "Carol",
        "age": 21,
        "major": "Physics",
        "gpa": 3.6,
    },
    "S004": {
        "name": "Dave",
        "age": 19,
        "major": "Biology",
        "gpa": 3.2,
    },
}

# -------------------------------------------------
# Step 2 — Print All Students (Outer + Inner Loop)
# Outer loop over students, inner loop over each student's info
# -------------------------------------------------
print("=" * 50)
print("PART 1 — Student Database")
print("=" * 50)
print("\nAll Students:")
print("-" * 30)

# Outer loop over students
for student_id, student_info in students.items():
    print(f"Student ID: {student_id}")
    # Inner loop over each student's info
    for key, value in student_info.items():
        print(f"  {key}: {value}")
    print()

# -------------------------------------------------
# Step 3 — Update a Student (use update() or assignment)
# Change S002's GPA from 3.4 to 3.7
# Change S002's major from "Math" to "Data Science"
# -------------------------------------------------
print("Step 3 — Updates:")
print("-" * 30)
students["S002"]["gpa"] = 3.7 # Update S002's GPA from 3.4 to 3.7
students["S002"]["major"] = "Data Science" # Update S002's major from "Math" to "Data Science"
print("Updated S002: GPA -> 3.7, major -> Data Science")
print()

# -------------------------------------------------
# Step 4 — Remove a Student (use pop())
# Remove S004 and store in removed_student
# -------------------------------------------------
print("Step 4 — Remove Student:")
print("-" * 30)
removed_student = students.pop("S004") # Remove S004 and store in removed_student
print("Removed student (S004):", removed_student)
print()

# -------------------------------------------------
# Step 5 — Search for a Student (use get())
# Search S003 (exists) and S999 (does not exist)
# -------------------------------------------------
print("Step 5 — Search for Students:")
print("-" * 30)

search_id_exists = "S003"
found_student = students.get(search_id_exists) # Search S003 and store in found_student
if found_student:
    print(f"Found {search_id_exists}: {found_student}")
else:
    print(f"Student {search_id_exists} not found.")

search_id_missing = "S999"
found_student = students.get(search_id_missing)
if found_student:
    print(f"Found {search_id_missing}: {found_student}")
else:
    print(f"Student {search_id_missing} not found.")
print()

# =====================================================
# PART 2 — COURSE ENROLLMENT USING SETS 
# =====================================================

# -------------------------------------------------
# Step 1 — Create Two Course Sets
# Each set with at least 3 names
# -------------------------------------------------
python_class = {"Alice", "Bob", "Carol"}
web_class = {"Bob", "Carol", "Dave"}

print("=" * 50)
print("PART 2 — Course Enrollment")
print("=" * 50)
print("\nInitial enrollment:")
print("python_class:", python_class)
print("web_class:", web_class)
print()

# -------------------------------------------------
# Step 2 — Add and Remove
# add() one new student to python_class
# discard() one student from web_class
# -------------------------------------------------
print("Step 2 — Add and Remove:")
print("-" * 30)
python_class.add("Eve") # Add Eve to python_class
print("After add('Eve') to python_class:", python_class)

web_class.discard("Dave") # Discard Dave from web_class
print("After discard('Dave') from web_class:", web_class)
print()

# -------------------------------------------------
# Step 3 — Set Operations
# intersection, union, difference (only in Python)
# -------------------------------------------------
print("Step 3 — Set Operations:")
print("-" * 30)

students_in_both = python_class.intersection(web_class) # Find students in both classes
print("Students in both classes (intersection):", students_in_both)

students_in_either = python_class.union(web_class) # Find students in either class
print("Students in either class (union):", students_in_either)

students_only_python = python_class.difference(web_class) # Find students only in Python
print("Students only in Python (difference):", students_only_python)
print()

# -------------------------------------------------
# Citations
# -------------------------------------------------
# Lab 07 assignment specifications
# Python documentation: dict.get(), dict.update(), dict.pop()
# Python documentation: set.add(), set.discard(), set.intersection(),
#   set.union(), set.difference()
