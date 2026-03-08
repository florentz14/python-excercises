# -------------------------------------------------
# File Name: 071_add_lists_from_left.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Add Two Lists from Left (element-wise, pad shorter with 0 or keep r...
# -------------------------------------------------

def add_lists_left(a: list[int], b: list[int]) -> list[int]:
    result = []
    for i in range(max(len(a), len(b))):
        # Asignación condicional: un valor u otro según la condición.
        x = a[i] if i < len(a) else 0
        # Asignación condicional: un valor u otro según la condición.
        y = b[i] if i < len(b) else 0
        result.append(x + y)
    return result


print(add_lists_left([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))  # [5, 7, 6, 7, 5, 8]
