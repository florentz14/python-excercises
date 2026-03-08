# -------------------------------------------------
# File Name: 36_binary_search.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Binary search on sorted list. Halves search space each step. O(log n).
# -------------------------------------------------

def binary_search(arr, target):
    """Iterative binary search. Returns index or -1 if not found."""
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Safe mid to avoid overflow
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_first(arr, target):
    """Returns index of first occurrence (for lists with duplicates)."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1   # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last(arr, target):
    """Returns index of last occurrence (for lists with duplicates)."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1   # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    print("=== Search Algorithms: Binary Search ===\n")

    arr = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print("Sorted list:", arr)
    print("Binary search for 5:", binary_search(arr, 5))
    print("First occurrence of 5:", binary_search_first(arr, 5))
    print("Last occurrence of 5:", binary_search_last(arr, 5))
