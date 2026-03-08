# -------------------------------------------------
# File Name: 31_two_sum_bruteforce.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Two Sum via nested loops, no extra data structures.
# -------------------------------------------------

def two_sum_bruteforce(arr: list[int], target: int) -> list[int]:
    """
    Finds two indices whose values sum to target.
    Compares each element with every other element.
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_bruteforce(arr, target)
    print(" ".join(map(str, res)))
