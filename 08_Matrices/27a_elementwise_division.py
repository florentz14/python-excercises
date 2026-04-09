# -------------------------------------------------
# File Name: 27a_elementwise_division.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Element-wise division of same-shape matrices.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


num = [[10, 20, 30], [40, 50, 60]]
den = [[2, 5, 5], [8, 10, 6]]
print_matrix(num, "Numerator")
print_matrix(den, "Denominator")
divided = [[num[i][j] / den[i][j] for j in range(len(num[0]))] for i in range(len(num))]
print_matrix(divided, "Element-wise division")
