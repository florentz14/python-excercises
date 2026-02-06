"""
Matrices - Ejemplo 3: Producto por escalar
==========================================
Tema: Matrices (08_Matrices)
Descripción: Multiplicar una matriz por un número (cada elemento * k).
"""

A = [[1, 2], [3, 4]]
k = 3

resultado = [[k * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("A =", A)
print("k =", k)
print("k * A =", resultado)
