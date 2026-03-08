# -------------------------------------------------
# File Name: 032_split_every_nth.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Split List Every Nth Element
# -------------------------------------------------

def split_every_nth(lst: list, n: int) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i::n] for i in range(n)]


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split_every_nth(sample, 3))
