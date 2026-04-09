# -------------------------------------------------
# File Name: 25b_trace.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Trace = sum of main diagonal.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(M, "Square matrix")
trace = sum(M[i][i] for i in range(len(M)))
print(f"Trace (diagonal sum): {trace}\n")
