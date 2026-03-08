# -------------------------------------------------
# File Name: 044_move_zeros_to_end.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Move All Zeros to End of List
# -------------------------------------------------

def move_zeros_end(lst: list[int]) -> list[int]:
    non_zero = [x for x in lst if x != 0]
    zeros = [0] * lst.count(0)
    return non_zero + zeros


sample = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7]
print(move_zeros_end(sample))
