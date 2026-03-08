# -------------------------------------------------
# File Name: 48_filter_integers_mixed.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Filter Integers from Mixed List (keep only int, not float)
# -------------------------------------------------

def filter_integers(lst: list) -> list[int]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]


sample = [34.67, 12, -94.89, 'Python', 0, 'C#']
print(filter_integers(sample))  # [12, 0]
