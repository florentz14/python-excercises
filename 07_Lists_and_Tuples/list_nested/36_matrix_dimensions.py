# -------------------------------------------------
# File Name: 36_matrix_dimensions.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Find Dimension of Matrix (rows, cols)
# -------------------------------------------------

def matrix_dimension(matrix: list[list]) -> tuple[int, int]:
    if not matrix:
        return (0, 0)
    # Se devuelve un valor u otro según la condición.
    return len(matrix), len(matrix[0]) if matrix[0] else 0


print(matrix_dimension([[1, 2], [2, 4]]))       # (2, 2)
print(matrix_dimension([[0, 1, 2], [2, 4, 5]]))  # (2, 3)
