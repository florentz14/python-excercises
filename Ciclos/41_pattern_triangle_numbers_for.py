# Patrón de números triangular
# Crear un triángulo de números donde cada fila tiene números del 1 hasta el número de la fila

print("Patrón Triangular de Números")
print("=" * 30)

# Loop externo: controla el número de filas (1 a 5)
for i in range(1, 6):
    # Loop interno: imprime números del 1 hasta i
    for j in range(1, i + 1):
        print(j, end=" ")
    # Nueva línea después de cada fila
    print()
