# 85. Create Multidimensional List with Zeros

def zeros_2d(rows: int, cols: int) -> list[list[int]]:
    return [[0] * cols for _ in range(rows)]


print(zeros_2d(3, 2))  # [[0, 0], [0, 0], [0, 0]]
