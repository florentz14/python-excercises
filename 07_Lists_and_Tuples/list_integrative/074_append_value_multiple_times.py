# -------------------------------------------------
# File Name: 074_append_value_multiple_times.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Append Same Value/List Multiple Times
# -------------------------------------------------

def append_times(value, n: int) -> list:
    # Se repite el valor length veces en una lista.
    return [value] * n


def append_list_times(lst: list, n: int) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[:] for _ in range(n)]


print(append_times(7, 5))  # [7, 7, 7, 7, 7]
print(append_list_times([1, 2, 5], 4))
