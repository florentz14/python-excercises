# Sumar elementos de una matriz 2D (tabla de números)
# Crear una matriz y sumar todos sus elementos

print("Suma de Elementos en una Matriz 2D")
print("=" * 40)

# Definir una matriz (lista de listas)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Variable para almacenar la suma total
total_sum = 0

# Loop externo: itera sobre cada fila de la matriz
for row in matrix:
    # Loop interno: itera sobre cada elemento en la fila
    for num in row:
        total_sum = total_sum + num

print("Matriz:")
# Mostrar la matriz
for row in matrix:
    print(row)

print(f"\nSuma total de elementos: {total_sum}")
