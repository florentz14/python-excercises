# -------------------------------------------------
# File Name: 09_multidimensional_zeros.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Create Multidimensional List with Zeros
# -------------------------------------------------

def zeros_2d(rows: int, cols: int) -> list[list[int]]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [[0] * cols for _ in range(rows)]


print(zeros_2d(3, 2))  # [[0, 0], [0, 0], [0, 0]]
