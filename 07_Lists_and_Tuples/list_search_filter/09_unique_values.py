# -------------------------------------------------
# File Name: 09_unique_values.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Get Unique Values from List (preserve order)
# -------------------------------------------------

def unique_values(lst: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(dict.fromkeys(lst))


print(unique_values([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]
