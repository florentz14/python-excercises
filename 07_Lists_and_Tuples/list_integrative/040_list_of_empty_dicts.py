# -------------------------------------------------
# File Name: 040_list_of_empty_dicts.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Create List of Empty Dictionaries
# -------------------------------------------------

def list_of_empty_dicts(n: int) -> list[dict]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [{} for _ in range(n)]


print(list_of_empty_dicts(5))  # [{}, {}, {}, {}, {}]
