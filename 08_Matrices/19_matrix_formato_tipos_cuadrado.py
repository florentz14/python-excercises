"""
08_Matrices - Imprimir en grid, matriz con tipos mixtos, verificar si es cuadrada
====================================================================================
Ejemplos 13-15.
"""

# Imprimir como grid
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz como grid:")
for row in grid:
    print(" ".join(str(x) for x in row))

# Matriz con tipos mixtos
mixed = [
    ["name", "age", "city"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"],
    ["Charlie", 28, "Chicago"],
]
print("\nMatriz mixta:")
for row in mixed:
    print(row)

# ¿Es cuadrada?
cuadrada = [[1, 2], [3, 4]]
rectangular = [[1, 2, 3], [4, 5, 6]]
print("\nMatriz cuadrada:", cuadrada, "-> es cuadrada:", len(cuadrada) == len(cuadrada[0]))
print("Matriz rectangular:", rectangular, "-> es cuadrada:", len(rectangular) == len(rectangular[0]))
