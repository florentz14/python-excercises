# -------------------------------------------------
# File Name: 127_remove_n_from_sides.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove n Elements from Left and Right
# -------------------------------------------------

def remove_from_sides(lst: list, n: int) -> tuple[list, list]:
    left_removed = lst[n:]
    # Asignación condicional: un valor u otro según la condición.
    right_removed = lst[:-n] if n > 0 else lst[:]
    return left_removed, right_removed


sample = [1, 2, 3, 4, 5, 6]
print(remove_from_sides(sample, 1))  # ([2,3,4,5,6], [1,2,3,4,5])
print(remove_from_sides(sample, 2))  # ([3,4,5,6], [1,2,3,4])
