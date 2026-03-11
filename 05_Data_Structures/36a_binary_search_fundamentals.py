# -------------------------------------------------
# File Name: 36a_binary_search_fundamentals.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Binary search fundamentals. Core concepts and templates.
# -------------------------------------------------

def binary_search_classic(arr: list[int], target: int) -> int:
    """
    Classic version. Uses mid = (left + right) // 2.
    Returns index of target, or -1 if not found.
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_optimized(arr: list[int], target: int) -> int:
    """
    Optimized and safe version.
    Uses mid = left + (right - left) // 2 to avoid overflow
    in languages such as C++/Java. Preferred in technical interviews.

    Returns index of target, or -1 if not found.
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Safer middle calculation

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search(arr: list[int], target: int, optimized: bool = True) -> int:
    """
    Wrapper that uses the optimized version by default.
    """
    return binary_search_optimized(arr, target) if optimized else binary_search_classic(arr, target)


# ------------------------------------------------------------
# Golden rule: Binary Search only works if the array is sorted.
# If not sorted: call sort(arr) first (costs O(n log n)).
# ------------------------------------------------------------


if __name__ == "__main__":
    # Basic example
    arr = [1, 3, 5, 7, 9, 11, 15]
    target = 7
    result = binary_search_optimized(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target} -> Index: {result}")

    # Search 11: Step 1 mid=7 (target>7) -> right; Step 2 mid=11 found
    target2 = 11
    result2 = binary_search_optimized(arr, target2)
    print(f"Target: {target2} -> Index: {result2}")

    # Not found
    target3 = 8
    result3 = binary_search_optimized(arr, target3)
    print(f"Target: {target3} -> Index: {result3} (not found)")

    # Version with user input (uncomment to use)
    # arr = [int(x) for x in input().split()]
    # target = int(input())
    # print(binary_search(arr, target))
