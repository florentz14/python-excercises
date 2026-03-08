# -------------------------------------------------
# File Name: 21_comprehension_practical.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Multiplication table, student grades table.
# -------------------------------------------------

mult = [[i * j for j in range(1, 5)] for i in range(1, 5)]
print("Multiplication table (4x4):")
for row in mult:
    print(row)

# Practical: grades by student (header + data rows)
grades = [
    ["Math", "Science", "English"],
    ["Alice", 85, 90, 88],
    ["Bob", 78, 88, 82],
    ["Charlie", 92, 95, 90],
]
print("\nGrades (header + rows):")
for row in grades:
    print(row)
print("Bob's Math:", grades[2][1])
print("Charlie's grades:", grades[3][1:])
