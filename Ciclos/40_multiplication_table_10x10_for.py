# Tabla de multiplicación completa (10x10)
# Mostrar la tabla de multiplicación del 1 al 10

print("Tabla de Multiplicación 10x10")
print("=" * 50)

# Loop externo: filas (números del 1 al 10)
for i in range(1, 11):
    # Loop interno: columnas (números del 1 al 10)
    for j in range(1, 11):
        # Mostrar el resultado sin salto de línea
        print(f"{i:2d} x {j:2d} = {i*j:3d}", end="  ")
    # Saltar a la siguiente línea después de cada fila
    print()
