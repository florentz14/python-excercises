# -------------------------------------------------
# File Name: 12_matrix_product.py
# Description: Matrix product of two matrices
# -------------------------------------------------

A = [[1, 2, 3], [4, 5, 6]]  # 2x3
B = [[-1, 0], [0, 1], [1, 1]]  # 3x2 -> result 2x2


def matmul(A, B):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible dimensions")
    C = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += A[i][k] * B[k][j]
    return C


result = matmul(A, B)
for row in result:
    print(row)
