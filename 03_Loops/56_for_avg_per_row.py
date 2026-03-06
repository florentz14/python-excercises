"""For loop: Average per row in matrix.
Computes sum and average for each row of a 2D matrix.
"""
# Author: Florentino Báez


print("Promedios por Fila en Matriz 2D")
print("=" * 40)

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Matriz:")
for row in matrix:
    print(row)

print("\nPromedios por fila:")

for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        row_sum = row_sum + matrix[i][j]
    average = row_sum / len(matrix[i])
    print(f"Fila {i}: suma = {row_sum}, promedio = {average}")
