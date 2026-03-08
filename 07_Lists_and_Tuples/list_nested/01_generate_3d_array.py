# -------------------------------------------------
# File Name: 01_generate_3d_array.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Generate 3*4*6 3D array with '*'
# -------------------------------------------------

def make_3d(h: int, w: int, d: int, fill: str = '*') -> list:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [[[fill for _ in range(d)] for _ in range(w)] for _ in range(h)]


arr = make_3d(3, 4, 6)
print(len(arr), len(arr[0]), len(arr[0][0]))  # 3 4 6
print(arr[0][0][0])  # *
