"""
Two Sum (Bruteforce) - No dictionary, double loop
=================================================
Topic: Operations (01_Variables_and_Types/operations)
Description: Basic approach, great for learning. Compare each number with all
others using nested loops. No extra data structures.

Input:  One line with space-separated numbers (the array).
        A second line with the target value.
Output: The two indices separated by space, or empty if no solution exists.

Complexity:
    - Time:   O(n²) - Two nested loops over the array
    - Space:  O(1)  - No extra memory (only loop variables)
"""


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
