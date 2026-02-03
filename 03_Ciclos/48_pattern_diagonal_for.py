# Patrón de matriz diagonal
# Crear una matriz donde mostramos la diagonal principal

print("Patrón de Diagonal")
print("=" * 30)

# Tamaño de la matriz (n x n)
size = 5

# Loop externo: itera sobre las filas
for i in range(size):
    # Loop interno: itera sobre las columnas
    for j in range(size):
        # Si el índice de fila es igual al de columna, es diagonal principal
        if i == j:
            print("X", end=" ")
        else:
            print(".", end=" ")
    # Nueva línea después de cada fila
    print()
