# -------------------------------------------------
# File Name: 36b_binary_search_interview_variants.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Binary search interview variants. Common LeetCode-style problems.
# -------------------------------------------------

def binary_search(arr: list[int], target: int) -> int:
    """
    1. Standard Binary Search
    Find the index of the target in a sorted array.
    Return -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def first_occurrence(arr: list[int], target: int) -> int:
    """
    2. First Occurrence
    If the number appears multiple times, return the FIRST position.
    Ex: [1,2,2,2,3,4], target=2 -> 1
    Idea: after finding the target, keep searching to the left.
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def last_occurrence(arr: list[int], target: int) -> int:
    """
    3. Last Occurrence
    If the number appears multiple times, return the LAST position.
    Ex: [1,2,2,2,3,4], target=2 -> 3
    Idea: after finding the target, keep searching to the right.
    """
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            answer = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


def search_insert_position(arr: list[int], target: int) -> int:
    """
    4. Search Insert Position
    If the number exists, return its index.
    If it does not exist, return the position where it should be inserted.
    Ex: [1,3,5,6], target=5->2, target=2->1, target=7->4
    Idea: if not found, left is the correct insertion position.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def find_peak(arr: list[int]) -> int:
    """
    5. Find Peak Element
    Find an element greater than its neighbors: arr[i] > arr[i-1] and arr[i] > arr[i+1].
    Ex: [1,3,20,4,1,0] -> 2 (because 20 > 3 and 20 > 4)
    Idea: if arr[mid] < arr[mid+1], slope is rising -> peak on the right.
          Otherwise, peak is on the left (including mid).
    """
    if not arr:
        return -1
    if len(arr) == 1:
        return 0

    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# Alias for consistency with previous names
peak_element = find_peak


def search_rotated_sorted(arr: list[int], target: int) -> int:
    """
    6. Search in Rotated Sorted Array
    Rotated sorted array: [4,5,6,7,0,1,2]
    At each step, one half is always sorted. Identify it and decide.
    """
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def find_boundary(arr: list[bool]) -> int:
    """
    7. Find First True (Boundary)
    Find the index of the first True in a boolean list [False, False, True, True].
    Returns -1 if no True. Binary search on predicate.
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index


# ------------------------------------------------------------
# Usage examples - Study order
# ------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. Standard Binary Search")
    print("=" * 55)
    arr = [1, 3, 5, 7, 9, 11]
    print(f"Array: {arr}")
    print(f"Target 7 -> index {binary_search(arr, 7)}")
    print(f"Target 8 -> index {binary_search(arr, 8)} (not found)")

    print("\n" + "=" * 55)
    print("2. First / 3. Last Occurrence")
    print("=" * 55)
    arr1 = [1, 2, 2, 2, 3, 4]
    print(f"Array: {arr1}")
    print(f"First occurrence of 2: {first_occurrence(arr1, 2)}")
    print(f"Last occurrence of 2:  {last_occurrence(arr1, 2)}")

    print("\n" + "=" * 55)
    print("4. Search Insert Position")
    print("=" * 55)
    arr2 = [1, 3, 5, 6]
    for t in [5, 2, 7, 0]:
        print(f"  Target {t} -> index {search_insert_position(arr2, t)}")

    print("\n" + "=" * 55)
    print("5. Find Peak Element")
    print("=" * 55)
    arr3 = [1, 3, 20, 4, 1, 0]
    idx = find_peak(arr3)
    print(f"Array: {arr3}")
    print(f"Peak at index {idx}, value {arr3[idx]} (20 > 3 and 20 > 4)")

    print("\n" + "=" * 55)
    print("6. Search in Rotated Sorted Array")
    print("=" * 55)
    arr4 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Array (rotated): {arr4}")
    for t in [0, 3, 5]:
        r = search_rotated_sorted(arr4, t)
        print(f"  Target {t} -> index {r}")

    print("\n" + "=" * 55)
    print("7. Find First True (Boundary)")
    print("=" * 55)
    arr5 = [False, False, True, True, True]
    print(f"Array: {arr5}")
    print(f"First True at index: {find_boundary(arr5)}")
