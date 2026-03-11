# -------------------------------------------------
# File Name: 36c_binary_search_workshop.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Binary search workshop. Practice problems and solutions.
# -------------------------------------------------

def ex1_binary_search(arr: list[int], target: int) -> int:
    """
    EXERCISE 1: Binary Search basic
    Find the index of target in a sorted array. Return -1 if it does not exist.
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


def ex2_first_occurrence(arr: list[int], target: int) -> int:
    """
    EXERCISE 2: First occurrence
    [1,2,2,2,3], target=2 → 1
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


def ex3_last_occurrence(arr: list[int], target: int) -> int:
    """
    EXERCISE 3: Last occurrence
    [1,2,2,2,3], target=2 → 3
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


def ex4_search_insert(arr: list[int], target: int) -> int:
    """
    EXERCISE 4: Search Insert Position
    [1,3,5,6], target=5→2, target=2→1, target=7→4
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
    return left


# =============================================================================
# LEVEL 2 - INTERMEDIATE (Exercises 5-7)
# =============================================================================

def ex5_sqrt(x: int) -> int:
    """
    EXERCISE 5: Square Root (Binary Search on Answer)
    Compute floor(sqrt(x)). Ex: x=8 -> 2, x=4 -> 2
    Idea: find the largest integer k such that k² <= x.
    """
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq < x:
            left = mid + 1
        else:
            right = mid - 1
    return right  # right is the largest integer with right² < x


def ex6_guess_number(n: int, pick: int) -> int:
    """
    EXERCISE 6: Guess Number Higher or Lower (LeetCode 374)
    Guess a number in [1..n]. The 'guess' API returns: -1 (too low), 0 (correct), 1 (too high).
    """
    def guess(num: int) -> int:
        if num < pick:
            return 1
        if num > pick:
            return -1
        return 0

    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        g = guess(mid)
        if g == 0:
            return mid
        if g == 1:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def ex7_search_rotated(arr: list[int], target: int) -> int:
    """
    EXERCISE 7: Search in Rotated Sorted Array
    [4,5,6,7,0,1,2], target=0 → 4
    """
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


# =============================================================================
# LEVEL 3 - UPPER-INTERMEDIATE (Exercises 8-9)
# =============================================================================

def ex8_find_peak(arr: list[int]) -> int:
    """
    EXERCISE 8: Find Peak Element
    [1,3,20,4,1] -> 2 (20 is a peak)
    """
    if len(arr) <= 1:
        return 0
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def ex9_first_bad_version(n: int, bad: int) -> int:
    """
    EXERCISE 9: First Bad Version (LeetCode 278)
    Versions 1..n. is_bad(v) is True if v>=bad. Find the first bad version.
    Ex: n=5, bad=4 -> 4
    """
    def is_bad_version(v: int) -> bool:
        return v >= bad

    left, right = 1, n
    answer = n
    while left <= right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


# =============================================================================
# LEVEL 4 - INTERVIEW (Exercise 10)
# =============================================================================

def ex10_min_in_rotated_sorted(arr: list[int]) -> int:
    """
    EXERCISE 10: Find Minimum in Rotated Sorted Array (LeetCode 153)
    [4,5,6,7,0,1,2] -> 0 (index 4)
    Return the minimum VALUE (not the index). Array has no duplicates.
    Idea: the minimum is to the left of the pivot. Compare mid with right.
    """
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]


def ex11_find_boundary(arr: list[bool]) -> int:
    """
    EXERCISE 11: Find First True (Boundary)
    [False, False, True, True] -> 2
    Binary search on boolean list. Input: space-separated "true"/"false".
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


# =============================================================================
# RUN AND VERIFICATION
# =============================================================================

def run_workshop():
    print("=" * 60)
    print("MINI WORKSHOP: 10 Binary Search Exercises")
    print("=" * 60)

    # Ex 1
    print("\n[1] Binary Search: arr=[1,3,5,7,9], target=7")
    print(f"    -> {ex1_binary_search([1, 3, 5, 7, 9], 7)} (expected: 3)")

    # Ex 2
    print("\n[2] First Occurrence: [1,2,2,2,3], target=2")
    print(f"    -> {ex2_first_occurrence([1, 2, 2, 2, 3], 2)} (expected: 1)")

    # Ex 3
    print("\n[3] Last Occurrence: [1,2,2,2,3], target=2")
    print(f"    -> {ex3_last_occurrence([1, 2, 2, 2, 3], 2)} (expected: 3)")

    # Ex 4
    print("\n[4] Search Insert: [1,3,5,6], targets 5,2,7")
    arr4 = [1, 3, 5, 6]
    for t in [5, 2, 7]:
        print(f"    target={t} -> {ex4_search_insert(arr4, t)}")

    # Ex 5
    print("\n[5] Sqrt(8), Sqrt(4)")
    print(f"    -> sqrt(8)={ex5_sqrt(8)}, sqrt(4)={ex5_sqrt(4)} (expected: 2, 2)")

    # Ex 6
    print("\n[6] Guess Number: n=10, pick=6")
    print(f"    -> {ex6_guess_number(10, 6)} (expected: 6)")

    # Ex 7
    print("\n[7] Search Rotated: [4,5,6,7,0,1,2], target=0")
    print(f"    -> {ex7_search_rotated([4, 5, 6, 7, 0, 1, 2], 0)} (expected: 4)")

    # Ex 8
    print("\n[8] Find Peak: [1,3,20,4,1]")
    arr8 = [1, 3, 20, 4, 1]
    idx8 = ex8_find_peak(arr8)
    print(f"    -> index {idx8}, value {arr8[idx8]} (expected: 2, 20)")

    # Ex 9
    print("\n[9] First Bad Version: n=5, bad=4")
    print(f"    -> {ex9_first_bad_version(5, 4)} (expected: 4)")

    # Ex 10
    print("\n[10] Min in Rotated: [4,5,6,7,0,1,2]")
    print(f"    -> {ex10_min_in_rotated_sorted([4, 5, 6, 7, 0, 1, 2])} (expected: 0)")

    # Ex 11
    print("\n[11] Find First True: [False,False,True,True,True]")
    print(f"    -> {ex11_find_boundary([False, False, True, True, True])} (expected: 2)")

    print("\n" + "=" * 60)
    print("Workshop completed. All O(log n).")
    print("=" * 60)


if __name__ == "__main__":
    run_workshop()


# Backward-compatible aliases.
ej1_binary_search = ex1_binary_search
ej2_first_occurrence = ex2_first_occurrence
ej3_last_occurrence = ex3_last_occurrence
ej4_search_insert = ex4_search_insert
ej5_sqrt = ex5_sqrt
ej6_guess_number = ex6_guess_number
ej7_search_rotated = ex7_search_rotated
ej8_find_peak = ex8_find_peak
ej9_first_bad_version = ex9_first_bad_version
ej10_min_in_rotated_sorted = ex10_min_in_rotated_sorted
ej11_find_boundary = ex11_find_boundary
