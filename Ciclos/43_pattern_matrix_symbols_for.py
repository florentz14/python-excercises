# Patrón de matriz rectangular (tabla de símbolos)
# Crear una matriz de 4 filas y 5 columnas con símbolos

print("Matriz Rectangular de Símbolos")
print("=" * 30)

# Filas de la matriz
rows = 4
# Columnas de la matriz
cols = 5

# Loop externo: itera sobre las filas
for i in range(rows):
    # Loop interno: itera sobre las columnas
    for j in range(cols):
        # Mostrar número de fila y columna
        print(f"[{i},{j}]", end=" ")
    # Nueva línea después de completar una fila
    print()
