"""
08_Matrices - Crear, mostrar, acceder y modificar matriz (lista de listas)
===========================================================================
Ejemplos 1-4: crear, acceso por índice, modificar elemento, dimensiones.
"""

# Crear y mostrar
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Matriz:")
for row in matrix:
    print(row)

# Acceso a elementos
print("\nElemento [0][0]:", matrix[0][0])
print("Elemento [1][2]:", matrix[1][2])
print("Elemento [2][1]:", matrix[2][1])

# Modificar
matrix[1][1] = 50
print("\nTras modificar [1][1] a 50:")
for row in matrix:
    print(row)

# Dimensiones
filas = len(matrix)
cols = len(matrix[0])
print(f"\nFilas: {filas}, Columnas: {cols}")
