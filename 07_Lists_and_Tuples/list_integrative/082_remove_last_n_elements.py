# -------------------------------------------------
# File Name: 082_remove_last_n_elements.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove Last N Elements from List
# -------------------------------------------------

def remove_last_n(lst: list, n: int) -> list:
    # Se devuelve un valor u otro según la condición.
    return lst[:-n] if n > 0 else lst[:]


sample = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
print(remove_last_n(sample, 3))
print(remove_last_n(sample, 5))
