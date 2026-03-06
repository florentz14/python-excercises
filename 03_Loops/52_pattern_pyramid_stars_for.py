# Patrón piramidal con asteriscos
# Crear una pirámide de asteriscos

print("Pirámide de Asteriscos")
print("=" * 30)

# Número de filas de la pirámide
rows = 5

# Loop externo: controla el número de filas
for i in range(1, rows + 1):
    # Loop interno: imprime asteriscos
    for j in range(i):
        print("*", end=" ")
    # Nueva línea después de cada fila
    print()
