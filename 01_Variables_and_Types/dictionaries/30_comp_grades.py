# -------------------------------------------------
# File Name: 30_comp_grades.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Grade statistics: compute averages in dict comprehension.
# -------------------------------------------------

print("10. Complex Example - Grade Statistics:")
print("-" * 60)
students = [
    ("Alice", [85, 90, 88]),
    ("Bob", [78, 82, 80]),
    ("Charlie", [92, 95, 93]),
    ("Diana", [88, 85, 90])
]

# Calculate average for each student
# Unpack tuple (name, grades), compute average with sum() and len()
averages = {
    name: sum(grades) / len(grades)
    for name, grades in students
}
print("Student averages:")
for name, avg in averages.items():
    print(f"  {name}: {avg:.2f}")
