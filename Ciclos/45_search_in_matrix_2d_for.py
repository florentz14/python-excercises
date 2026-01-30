# Buscar un elemento en una matriz 2D
# Recorrer una matriz y encontrar la posición de un número específico

print("Búsqueda en Matriz 2D")
print("=" * 40)

# Definir una matriz
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Número que buscamos
search_value = 50
found = False
found_row = -1
found_col = -1

# Loop externo: itera sobre las filas con índice
for i in range(len(matrix)):
    # Loop interno: itera sobre las columnas con índice
    for j in range(len(matrix[i])):
        # Verificar si encontramos el número
        if matrix[i][j] == search_value:
            found = True
            found_row = i
            found_col = j
            break
    # Si encontramos el número, salir del loop externo
    if found:
        break

# Mostrar resultados
print("Matriz:")
for row in matrix:
    print(row)

if found:
    print(
        f"\nValor {search_value} encontrado en posición [{found_row}][{found_col}]")
else:
    print(f"\nValor {search_value} no encontrado en la matriz")
