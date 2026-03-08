# -------------------------------------------------
# File Name: 62_has_duplicates.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If List Has Duplicate Values
# -------------------------------------------------

def has_duplicates(lst: list) -> bool:
    # Se devuelve la cantidad de elementos.
    return len(lst) != len(set(lst))


print(has_duplicates([1, 2, 3, 4, 5, 6, 7]))   # False
print(has_duplicates([1, 2, 3, 3, 4, 5, 5]))  # True
