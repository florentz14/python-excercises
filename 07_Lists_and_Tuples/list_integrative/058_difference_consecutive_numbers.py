# -------------------------------------------------
# File Name: 058_difference_consecutive_numbers.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Difference Between Consecutive Numbers (lst[i+1] - lst[i])
# -------------------------------------------------

def consecutive_diffs(lst: list[int | float]) -> list[int | float]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]


print(consecutive_diffs([1, 1, 3, 4, 4, 5, 6, 7]))  # [0, 2, 1, 0, 1, 1, 1]
print(consecutive_diffs([4, 5, 8, 9, 6, 10]))       # [1, 3, 1, -3, 4]
