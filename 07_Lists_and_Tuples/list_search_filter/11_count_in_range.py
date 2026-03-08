# -------------------------------------------------
# File Name: 11_count_in_range.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Count Elements in List Within Specified Range
# -------------------------------------------------

def count_in_range(lst: list[int | float], low: int | float, high: int | float) -> int:
    # Se devuelve la suma de todos los elementos.
    return sum(1 for x in lst if low <= x <= high)


print(count_in_range([1, 5, 3, 7, 2, 9], 2, 6))  # 4
