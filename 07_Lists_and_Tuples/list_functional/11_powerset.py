# -------------------------------------------------
# File Name: 11_powerset.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Powerset of Iterable
# -------------------------------------------------

import itertools

def powerset(iterable) -> list[tuple]:
    s = list(iterable)
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [tuple(c) for r in range(len(s) + 1) for c in itertools.combinations(s, r)]


print(powerset([1, 2]))
print(len(powerset([1, 2, 3, 4])))  # 16
