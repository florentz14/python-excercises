# Encontrar máximo en matriz 2D
# Recorrer una matriz y encontrar el valor máximo

print("Encontrar Máximo en Matriz 2D")
print("=" * 40)

# Definir una matriz
matrix = [
    [15, 42, 8],
    [99, 23, 56],
    [45, 67, 12]
]

# Inicializar el máximo con el primer elemento
max_value = matrix[0][0]
max_row = 0
max_col = 0

print("Matriz:")
for row in matrix:
    print(row)

print("\nBuscando máximo...")

# Loop externo: itera sobre las filas con índice
for i in range(len(matrix)):
    # Loop interno: itera sobre las columnas con índice
    for j in range(len(matrix[i])):
        # Comparar si el elemento actual es mayor que el máximo
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

print(f"\nValor máximo: {max_value}")
print(f"Posición: [{max_row}][{max_col}]")
