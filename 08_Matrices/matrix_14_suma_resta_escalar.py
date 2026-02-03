"""
08_Matrices - Suma, resta y producto por escalar
=================================================
Ejemplos 1-3 de matrix_operations: A+B, A-B, k*A.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print_matrix(A, "A")
print_matrix(B, "B")

# Suma
suma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print_matrix(suma, "A + B")

# Resta
resta = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print_matrix(resta, "A - B")

# Producto por escalar
k = 2
resultado = [[x * k for x in row] for row in A]
print_matrix(resultado, f"A x {k}")
