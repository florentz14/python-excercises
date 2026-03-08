# -------------------------------------------------
# File Name: 12_common_items_two_lists.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Find Common Items in Two Lists
# -------------------------------------------------

def common_items(a: list, b: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(set(a) & set(b))


print(common_items([1, 2, 3], [2, 3, 4]))  # [2, 3]
