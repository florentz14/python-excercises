# Patrón de cuadrado (rectángulo de símbolos)
# Crear un cuadrado/rectángulo usando caracteres

print("Patrón de Cuadrado")
print("=" * 30)

# Dimensiones del cuadrado
size = 5

# Loop externo: controla las filas
for i in range(size):
    # Loop interno: controla las columnas
    for j in range(size):
        print("*", end=" ")
    # Nueva línea después de cada fila
    print()
