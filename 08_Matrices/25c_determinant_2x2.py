# -------------------------------------------------
# File Name: 25c_determinant_2x2.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Determinant 2x2: ad - bc.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


M2 = [[4, 7], [2, 6]]
print_matrix(M2, "2x2 matrix")
det = M2[0][0] * M2[1][1] - M2[0][1] * M2[1][0]
print(f"Determinant = (4*6) - (7*2) = {det}")
