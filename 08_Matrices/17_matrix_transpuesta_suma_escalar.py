"""
08_Matrices - Transpuesta, suma de matrices y producto por escalar
===================================================================
Ejemplos 7-9: transponer, A+B, k*A.
"""

# Transpuesta
original = [[1, 2, 3], [4, 5, 6]]
print("Matriz original (2x3):")
for row in original:
    print(row)
transpuesta = [
    [original[i][j] for i in range(len(original))]
    for j in range(len(original[0]))
]
print("Transpuesta (3x2):")
for row in transpuesta:
    print(row)

# Suma de matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
suma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("\nA + B:")
for row in suma:
    print(row)

# Producto por escalar
k = 2
M = [[1, 2], [3, 4]]
resultado = [[x * k for x in row] for row in M]
print(f"\n{k} * M:")
for row in resultado:
    print(row)
