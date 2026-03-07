# ------------------------------------------------------------
# File: 91_set_matrix_zeroes.py
# Purpose: Set matrix zeroes.
# Description: If M[i][j]==0, set entire row i and column j to 0.
# ------------------------------------------------------------

def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in zero_rows:
        for c in range(n):
            matrix[r][c] = 0
    for c in zero_cols:
        for r in range(m):
            matrix[r][c] = 0

m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("Before:", m)
set_zeroes(m)
print("After:", m)
