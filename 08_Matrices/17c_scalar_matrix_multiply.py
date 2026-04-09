# -------------------------------------------------
# File Name: 17c_scalar_matrix_multiply.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Multiply every entry of a matrix by a scalar.
# -------------------------------------------------

k = 2
M = [[1, 2], [3, 4]]
scaled = [[x * k for x in row] for row in M]
print(f"{k} * M:")
for row in scaled:
    print(row)
