# -------------------------------------------------
# File Name: 32_two_sum_numpy.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Two Sum using NumPy - double loop and sums matrix approaches.
# -------------------------------------------------

import numpy as np


def two_sum_numpy_basic(arr, target: int) -> list[int]:
    """NumPy + double loop. Same as bruteforce but with np.array."""
    arr = np.array(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


def two_sum_numpy_matrix(arr, target: int) -> list[int]:
    """
    NumPy style: build matrix of all pairwise sums.
    sums[i, j] = arr[i] + arr[j] via broadcasting (arr[:, None] + arr).
    """
    arr = np.array(arr)
    sums = arr[:, None] + arr
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if sums[i, j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())

    res = two_sum_numpy_basic(arr, target)  # or two_sum_numpy_matrix(arr, target)
    print(" ".join(map(str, res)))
