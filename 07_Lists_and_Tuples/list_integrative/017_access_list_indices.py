# -------------------------------------------------
# File Name: 017_access_list_indices.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Access the Index of a List
# -------------------------------------------------

def with_index(lst: list) -> list[tuple[int, any]]:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(enumerate(lst))


sample = ['a', 'b', 'c']
for i, v in with_index(sample):
    print(i, v)
