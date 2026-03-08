# -------------------------------------------------
# File Name: 042_insert_string_before_items.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Insert String at Beginning of All Items. [1,2,3,4], 'emp' -> ['emp1...
# -------------------------------------------------

def prefix_items(lst: list, prefix: str) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [f"{prefix}{x}" for x in lst]


print(prefix_items([1, 2, 3, 4], 'emp'))
