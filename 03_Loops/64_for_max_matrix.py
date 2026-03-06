"""For loop: Find max in 2D matrix.
Finds maximum value and its position.
"""
# Author: Florentino Báez


print("Encontrar Máximo en Matriz 2D")
print("=" * 40)

matrix = [
    [15, 42, 8],
    [99, 23, 56],
    [45, 67, 12]
]

max_value = matrix[0][0]
max_row = 0
max_col = 0

print("Matriz:")
for row in matrix:
    print(row)

print("\nBuscando máximo...")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

print(f"\nValor máximo: {max_value}")
print(f"Posición: [{max_row}][{max_col}]")
