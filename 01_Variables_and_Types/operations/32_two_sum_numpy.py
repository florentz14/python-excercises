"""
Two Sum (NumPy) - Two approaches using NumPy
============================================
Topic: Operations (01_Variables_and_Types/operations)
Description: NumPy is not ideal for Two Sum (dictionary or bruteforce are
usually better), but it can be done for comparison purposes.

Option A: NumPy + double loop - Same logic as bruteforce, array as np.ndarray.
Option B: Matrix of sums - More "NumPy style", builds sums[i,j] = arr[i]+arr[j],
          but uses more memory (O(n²) for the matrix).

Input:  One line with space-separated numbers (the array).
        A second line with the target value.
Output: The two indices separated by space, or empty if no solution exists.

Complexity:
    - Option A: Time O(n²), Space O(n) for the numpy array
    - Option B: Time O(n²), Space O(n²) for the sums matrix
"""

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
