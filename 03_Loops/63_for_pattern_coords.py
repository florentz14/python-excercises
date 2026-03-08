# -------------------------------------------------
# File Name: 63_for_pattern_coords.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Coordinate pattern.
# -------------------------------------------------

print("Tabla de Posiciones (Coordenadas)")
print("=" * 40)

rows = 3
cols = 4

print("Matriz de posiciones [fila, columna]:\n")

for i in range(rows):
    for j in range(cols):
        print(f"[{i},{j}]", end="  ")
    print()
