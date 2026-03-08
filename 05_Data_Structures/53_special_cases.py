# -------------------------------------------------
# File Name: 53_special_cases.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Special cases in sorting. Edge cases and optimizations.
# -------------------------------------------------

def is_sorted(arr):
    """Returns True if the list is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def merge(left, right):
    """Merges two sorted lists into one sorted list (two-pointer merge)."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    """Merge Sort: divide in half, sort recursively, merge. O(n log n)."""
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def test_special_cases():
    """Runs Merge Sort on edge cases and verifies correctness."""
    cases = {
        "Already sorted":   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Reverse sorted":   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "All equal":        [5, 5, 5, 5, 5, 5],
        "Single element":   [42],
        "Empty":            [],
    }
    print("\nSpecial cases (Merge Sort):")
    print("=" * 70)
    for name, case in cases.items():
        print(f"\n{name}: {case}")
        if case:
            result = merge_sort(case)
            print(f"  Sorted:   {result}")
            print(f"  Verified: {'OK' if is_sorted(result) else 'FAIL'}")
        else:
            print("  Empty list - no sorting needed")


if __name__ == "__main__":
    print("=== Special Cases - Merge Sort ===\n")
    test_special_cases()
