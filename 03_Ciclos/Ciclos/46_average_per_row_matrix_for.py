# Promedios por fila en una matriz
# Calcular el promedio de cada fila en una matriz

print("Promedios por Fila en Matriz 2D")
print("=" * 40)

# Definir una matriz
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Matriz:")
for row in matrix:
    print(row)

print("\nPromedios por fila:")

# Loop externo: itera sobre cada fila
for i in range(len(matrix)):
    row_sum = 0

    # Loop interno: suma todos los elementos de la fila
    for j in range(len(matrix[i])):
        row_sum = row_sum + matrix[i][j]

    # Calcular promedio
    average = row_sum / len(matrix[i])
    print(f"Fila {i}: suma = {row_sum}, promedio = {average}")
