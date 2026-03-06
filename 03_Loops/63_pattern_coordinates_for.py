# Patrón de tabla de posiciones (coordenadas)
# Mostrar una tabla con las posiciones de cada elemento

print("Tabla de Posiciones (Coordenadas)")
print("=" * 40)

# Dimensiones
rows = 3
cols = 4

print("Matriz de posiciones [fila, columna]:\n")

# Loop externo: itera sobre las filas
for i in range(rows):
    # Loop interno: itera sobre las columnas
    for j in range(cols):
        print(f"[{i},{j}]", end="  ")
    # Nueva línea después de cada fila
    print()
