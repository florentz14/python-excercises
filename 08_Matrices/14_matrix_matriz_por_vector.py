"""
Matrices - Ejemplo 6: Matriz por vector (columna)
==================================================
Tema: Matrices (08_Matrices)
Descripción: A (m×n) * v (n×1) = vector de m componentes. Cada fila de A · v.
"""

A = [[1, 2], [3, 4], [5, 6]]  # 3x2
v = [7, 8]                      # vector de 2 componentes

# Resultado: para cada fila i, suma A[i][k] * v[k]
resultado = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]
print("A =")
for fila in A:
    print(" ", fila)
print("v =", v)
print("A * v =", resultado)
