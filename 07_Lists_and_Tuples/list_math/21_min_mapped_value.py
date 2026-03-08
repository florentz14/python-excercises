# -------------------------------------------------
# File Name: 21_min_mapped_value.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Min Value After Mapping
# -------------------------------------------------

def min_after_map(lst: list, func) -> int | float:
    return min(func(x) for x in lst)


print(min_after_map([1, 2, 3, 4], lambda x: x * 2))  # 2
