# Contar filas y columnas en una matriz
# Recorrer una matriz y contar el número total de elementos

print("Contar Elementos en Matriz 2D")
print("=" * 40)

# Definir una matriz
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Variables para contar
total_elements = 0
rows_count = 0

# Loop externo: itera sobre cada fila
for row in matrix:
    rows_count = rows_count + 1
    # Loop interno: itera sobre cada elemento en la fila
    for element in row:
        total_elements = total_elements + 1

print("Matriz:")
for row in matrix:
    print(row)

print(f"\nNúmero de filas: {rows_count}")
print(f"Número de columnas: {len(matrix[0])}")
print(f"Total de elementos: {total_elements}")
