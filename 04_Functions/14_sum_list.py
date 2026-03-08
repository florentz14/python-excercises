# -------------------------------------------------
# File Name: 14_sum_list.py
# Author: Florentino Báez
# Date: 04_Functions
# Description: Sum all elements in a list.
# -------------------------------------------------

def sum_list(numbers: list[int | float]) -> None:
    total = 0
    for n in numbers:
        total += n
    print(total)


sum_list([2, 4, 6, 8])
