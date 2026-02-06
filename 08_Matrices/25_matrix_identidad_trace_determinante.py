"""
08_Matrices - Identidad × matriz, traza y determinante 2×2
==========================================================
Ejemplos 9-11: H×I, traza (suma diagonal), det 2x2.
"""


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


# Identidad × matriz (H × I = H)
I = [[1, 0], [0, 1]]
H = [[5, 6], [7, 8]]
print_matrix(I, "I (2x2)")
print_matrix(H, "H")
result = []
for i in range(len(H)):
    row = []
    for j in range(len(I[0])):
        row.append(sum(H[i][k] * I[k][j] for k in range(len(I))))
    result.append(row)
print_matrix(result, "H x I")

# Traza (suma de la diagonal)
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(M, "Matriz cuadrada")
traza = sum(M[i][i] for i in range(len(M)))
print(f"Traza (suma diagonal): {traza}\n")

# Determinante 2x2
M2 = [[4, 7], [2, 6]]
print_matrix(M2, "Matriz 2x2")
det = M2[0][0] * M2[1][1] - M2[0][1] * M2[1][0]
print(f"Determinante = (4×6) - (7×2) = {det}")
