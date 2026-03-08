# -------------------------------------------------
# File Name: 26_row_column_sums.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Sum all elements, sum per row, sum per column.
# -------------------------------------------------

def print_matrix(matrix, name="Matrix"):
    """Print matrix with aligned columns."""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:5}" for x in row])
    print()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(A, "A")
print("Total sum:", sum(sum(row) for row in A))

# Row sums
row_sums = [sum(row) for row in A]
print("Row sums:", row_sums)

# Column sums
col_sums = [sum(A[i][j] for i in range(len(A))) for j in range(len(A[0]))]
print("Column sums:", col_sums)
