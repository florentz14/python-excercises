# -------------------------------------------------
# File Name: 021_concatenate_list_with_range.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Create List by Concatenating List with Range 1 to n
# -------------------------------------------------

def concat_with_range(lst: list, n: int) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [f"{item}{i}" for i in range(1, n + 1) for item in lst]


print(concat_with_range(['p', 'q'], 5))
