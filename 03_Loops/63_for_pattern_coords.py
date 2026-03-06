"""For loop: Coordinate pattern.
Prints [row,col] for each cell in grid.
"""
# Author: Florentino Báez


print("Tabla de Posiciones (Coordenadas)")
print("=" * 40)

rows = 3
cols = 4

print("Matriz de posiciones [fila, columna]:\n")

for i in range(rows):
    for j in range(cols):
        print(f"[{i},{j}]", end="  ")
    print()
