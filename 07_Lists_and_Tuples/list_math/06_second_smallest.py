# -------------------------------------------------
# File Name: 06_second_smallest.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Find Second Smallest Number in List
# -------------------------------------------------

def second_smallest(lst: list[int | float]) -> int | float:
    uniq = sorted(set(lst))
    # Se devuelve un valor u otro según la condición.
    return uniq[1] if len(uniq) > 1 else uniq[0]


print(second_smallest([1, 2, 3, 4, 5]))  # 2
