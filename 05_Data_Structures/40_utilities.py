# -------------------------------------------------
# File Name: 40_utilities.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Sorting utilities. Helper functions for sort implementations.
# -------------------------------------------------

def binary_search_first(arr, target):
    """Returns index of first occurrence, or -1 if not found."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last(arr, target):
    """Returns index of last occurrence, or -1 if not found."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def find_insert_position(arr, target):
    """Position to insert target to maintain sorted order (bisect_left)."""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def count_occurrences(arr, target):
    """Counts how many times target appears in sorted arr. O(log n)."""
    first = binary_search_first(arr, target)
    if first == -1:
        return 0
    last = binary_search_last(arr, target)
    return last - first + 1


if __name__ == "__main__":
    print("=== Search Utilities: Sorted List Helpers ===\n")

    arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6]
    print("List:", arr)
    print("Insert position for 3:", find_insert_position(arr, 3))
    print("Count of 5s:", count_occurrences(arr, 5))
