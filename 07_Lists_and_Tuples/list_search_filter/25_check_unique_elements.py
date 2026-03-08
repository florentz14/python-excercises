# -------------------------------------------------
# File Name: 25_check_unique_elements.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If All Elements in List Are Unique
# -------------------------------------------------

def all_unique(lst: list) -> bool:
    # Se devuelve la cantidad de elementos.
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 4, 6, 8]))   # True
print(all_unique([1, 2, 4, 6, 8, 2]))  # False
