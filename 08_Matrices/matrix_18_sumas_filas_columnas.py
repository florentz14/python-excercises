"""
08_Matrices - Suma total, sumas por fila y por columna
=======================================================
Ejemplos 12-13.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(A, "A")
print("Suma de todos los elementos:", sum(sum(row) for row in A))

# Sumas por fila
filas_suma = [sum(row) for row in A]
print("Sumas por fila:", filas_suma)

# Sumas por columna
cols_suma = [sum(A[i][j] for i in range(len(A))) for j in range(len(A[0]))]
print("Sumas por columna:", cols_suma)
