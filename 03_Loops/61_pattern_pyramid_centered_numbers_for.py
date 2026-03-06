# Patrón de pirámide centrada con números
# Crear una pirámide centrada mostrando números

print("Pirámide Centrada con Números")
print("=" * 40)

# Número de filas
size = 5

# Loop externo: controla las filas (1 a size)
for i in range(1, size + 1):
    # Espacios en blanco para centrar (size - i espacios)
    for space in range(size - i):
        print(" ", end=" ")

    # Loop interno: imprime números del 1 hasta i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Nueva línea después de cada fila
    print()
