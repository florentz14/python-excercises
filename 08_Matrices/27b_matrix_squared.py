# -------------------------------------------------
# File Name: 27b_matrix_squared.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Matrix product I * I (square), not element-wise.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


I = [[1, 2], [3, 4]]
print_matrix(I, "I")
I2 = [[sum(I[i][k] * I[k][j] for k in range(len(I))) for j in range(len(I[0]))] for i in range(len(I))]
print_matrix(I2, "I squared (I * I)")
