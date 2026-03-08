# -------------------------------------------------
# File Name: 105_build_list_with_iterator.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Build List Using Iterator and Seed (e.g. -10, -20, -30, -40)
# -------------------------------------------------

def build_list(seed, func, n: int) -> list:
    result = []
    x = seed
    for _ in range(n):
        result.append(x)
        x = func(x)
    return result


print(build_list(-10, lambda x: x - 10, 4))  # [-10, -20, -30, -40]
