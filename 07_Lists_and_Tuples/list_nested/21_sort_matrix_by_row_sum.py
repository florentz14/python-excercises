# -------------------------------------------------
# File Name: 21_sort_matrix_by_row_sum.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Sort Matrix by Row Sum (ascending)
# -------------------------------------------------

def sort_matrix_by_row_sum(matrix: list[list[int]]) -> list[list[int]]:
    # Se ordena la lista usando key para comparar (p. ej. por longitud o valor).
    return sorted(matrix, key=sum)


sample = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix_by_row_sum(sample))  # [[1,1,1], [1,2,3], [2,4,5]]
