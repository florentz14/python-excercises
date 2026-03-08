# -------------------------------------------------
# File Name: 54_for_sum_matrix.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Sum 2D matrix elements.
# -------------------------------------------------

print("Suma de Elementos en una Matriz 2D")
print("=" * 40)

# Define a 3x3 matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total_sum = 0

# Outer loop: each row
for row in matrix:
    # Inner loop: each element in row
    for num in row:
        total_sum = total_sum + num

print("Matriz:")
for row in matrix:
    print(row)

print(f"\nSuma total de elementos: {total_sum}")
