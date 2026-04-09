# -------------------------------------------------
# File Name: 25a_identity_times_matrix.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: H * I = H for 2x2 identity I.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


I = [[1, 0], [0, 1]]
H = [[5, 6], [7, 8]]
print_matrix(I, "I (2x2)")
print_matrix(H, "H")
result = [[sum(H[i][k] * I[k][j] for k in range(len(I))) for j in range(len(I[0]))] for i in range(len(H))]
print_matrix(result, "H * I")
