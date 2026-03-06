"""For loop: Search in 2D matrix.
Finds value position; breaks both loops when found.
"""
# Author: Florentino Báez


print("Búsqueda en Matriz 2D")
print("=" * 40)

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

search_value = 50
found = False
found_row = -1
found_col = -1

# Iterate with indices to get position
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == search_value:
            found = True
            found_row = i
            found_col = j
            break
    if found:
        break

print("Matriz:")
for row in matrix:
    print(row)

if found:
    print(f"\nValor {search_value} encontrado en posición [{found_row}][{found_col}]")
else:
    print(f"\nValor {search_value} no encontrado en la matriz")
