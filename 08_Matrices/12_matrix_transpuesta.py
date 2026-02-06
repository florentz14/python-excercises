"""
Matrices - Ejemplo 4: Transpuesta
=================================
Tema: Matrices (08_Matrices)
Descripción: A^T: intercambiar filas por columnas. Si A es m×n, A^T es n×m.
"""

A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpuesta: fila j de A^T = columna j de A
filas, cols = len(A), len(A[0])
transpuesta = [[A[i][j] for i in range(filas)] for j in range(cols)]

print("A =")
for fila in A:
    print(" ", fila)
print("A^T (transpuesta) =")
for fila in transpuesta:
    print(" ", fila)
