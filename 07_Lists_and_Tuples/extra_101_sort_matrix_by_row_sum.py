# 101. Sort Matrix by Row Sum (ascending)

def sort_matrix_by_row_sum(matrix: list[list[int]]) -> list[list[int]]:
    return sorted(matrix, key=sum)


sample = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix_by_row_sum(sample))  # [[1,1,1], [1,2,3], [2,4,5]]
