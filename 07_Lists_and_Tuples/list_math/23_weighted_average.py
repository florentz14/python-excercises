# -------------------------------------------------
# File Name: 23_weighted_average.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Weighted Average of Numbers
# -------------------------------------------------

def weighted_average(values: list[float], weights: list[float]) -> float:
    # Se devuelve un valor u otro según la condición.
    return sum(v * w for v, w in zip(values, weights)) / sum(weights) if sum(weights) else 0


print(weighted_average([10, 50, 40], [2, 5, 3]))  # 39.0
