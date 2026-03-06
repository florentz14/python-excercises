"""For loop: Count matrix elements.
Counts rows and total elements in a 2D matrix.
"""
# Author: Florentino Báez


print("Contar Elementos en Matriz 2D")
print("=" * 40)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

total_elements = 0
rows_count = 0

for row in matrix:
    rows_count = rows_count + 1
    for element in row:
        total_elements = total_elements + 1

print("Matriz:")
for row in matrix:
    print(row)

print(f"\nNúmero de filas: {rows_count}")
print(f"Número de columnas: {len(matrix[0])}")
print(f"Total de elementos: {total_elements}")
