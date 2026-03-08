# -------------------------------------------------
# File Name: 92_search_2d_matrix.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Rows and columns sorted. Search for target in O(m+n).
# -------------------------------------------------

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        if val > target:
            c -= 1
        else:
            r += 1
    return False

m = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
print("Matrix:")
for row in m:
    print(row)
print("Search 5:", search_matrix(m, 5))
print("Search 10:", search_matrix(m, 10))
