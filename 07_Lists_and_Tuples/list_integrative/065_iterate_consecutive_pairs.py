# -------------------------------------------------
# File Name: 065_iterate_consecutive_pairs.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Iterate Over All Pairs of Consecutive Items
# -------------------------------------------------

def consecutive_pairs(lst: list) -> list[tuple]:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(zip(lst[:-1], lst[1:]))


sample = [1, 1, 2, 3, 3, 4, 4, 5]
print(consecutive_pairs(sample))
