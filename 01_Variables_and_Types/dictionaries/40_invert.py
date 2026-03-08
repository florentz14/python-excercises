# -------------------------------------------------
# File Name: 40_invert.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Group records by key fields (grade, subject) using defaultdict.
# -------------------------------------------------

students = [
    {'name': 'Alice', 'grade': 'A', 'subject': 'Math'},
    {'name': 'Bob', 'grade': 'B', 'subject': 'Math'},
    {'name': 'Charlie', 'grade': 'A', 'subject': 'Science'},
    {'name': 'David', 'grade': 'C', 'subject': 'Math'},
    {'name': 'Eve', 'grade': 'B', 'subject': 'Science'},
]

# Group by grade
from collections import defaultdict

grouped_by_grade = defaultdict(list)
for student in students:
    grouped_by_grade[student['grade']].append(student)

print("Grouped by grade:")
for grade, students_list in grouped_by_grade.items():
    print(f"  {grade}: {[s['name'] for s in students_list]}")

# Group by subject
grouped_by_subject = defaultdict(list)
for student in students:
    grouped_by_subject[student['subject']].append(student)

print("\nGrouped by subject:")
for subject, students_list in grouped_by_subject.items():
    print(f"  {subject}: {[s['name'] for s in students_list]}")

# Nested grouping: subject -> grade -> students
nested_group = defaultdict(lambda: defaultdict(list))
for student in students:
    nested_group[student['subject']][student['grade']].append(student['name'])

print("\nNested grouping (subject -> grade -> names):")
for subject, grades in nested_group.items():
    print(f"  {subject}:")
    for grade, names in grades.items():
        print(f"    {grade}: {names}")