"""
Matrices - Ejemplo 1: Crear y mostrar una matriz
================================================
Tema: Matrices (08_Matrices)
Descripción: Representar una matriz como lista de listas (filas).
"""

# Matriz 2x3: 2 filas, 3 columnas
A = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Matriz A (2x3):")
for fila in A:
    print(" ", fila)
print("Filas:", len(A))
print("Columnas:", len(A[0]))
print("Elemento A[1][2] =", A[1][2])  # fila 1, columna 2
