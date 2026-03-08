# -------------------------------------------------
# File Name: 50_non_unique_filtered_out.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: List with Non-Unique Values Filtered Out (keep only unique)
# -------------------------------------------------

def only_unique(lst: list) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if lst.count(x) == 1]


print(only_unique([1, 2, 2, 3, 4, 4, 5]))  # [1, 3, 5]
