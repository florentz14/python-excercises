# -------------------------------------------------
# File Name: 45_indexes_of_none.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Find Indexes of All None Items in List
# -------------------------------------------------

def indexes_of_none(lst: list) -> list[int]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [i for i, x in enumerate(lst) if x is None]


sample = [1, None, 5, 4, None, 0, None, None]
print(indexes_of_none(sample))  # [1, 4, 6, 7]
