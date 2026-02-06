"""
Matrices - Ejemplo 2: Suma de matrices
======================================
Tema: Matrices (08_Matrices)
Descripción: Sumar dos matrices del mismo tamaño elemento a elemento.
"""

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# A + B: misma dimensión
filas, cols = len(A), len(A[0])
suma = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(filas)]

print("A =", A)
print("B =", B)
print("A + B =", suma)
