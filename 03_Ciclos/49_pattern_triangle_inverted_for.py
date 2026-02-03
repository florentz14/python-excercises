# Patrón de triángulo invertido
# Crear un triángulo invertido de números

print("Triángulo Invertido")
print("=" * 30)

# Número inicial de columnas
size = 5

# Loop externo: controla las filas (de size a 1)
for i in range(size, 0, -1):
    # Loop interno: imprime i números
    for j in range(1, i + 1):
        print(j, end=" ")
    # Nueva línea después de cada fila
    print()
