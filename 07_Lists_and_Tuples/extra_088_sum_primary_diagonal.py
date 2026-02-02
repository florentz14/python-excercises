# 88. Sum of Primary Diagonal of Square Matrix

def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


# 3x3: [[2,3,4],[4,5,6],[3,4,7]] -> 2+5+7 = 14
m = [[2, 3, 4], [4, 5, 6], [3, 4, 7]]
print(sum_primary_diagonal(m))  # 14
