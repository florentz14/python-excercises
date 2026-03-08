# -------------------------------------------------
# File Name: 01_generate_permutations.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Generate All Permutations of a List
# -------------------------------------------------

import itertools

def all_permutations(lst: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(itertools.permutations(lst))


sample = [1, 2, 3]
print(all_permutations(sample))
