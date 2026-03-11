# -------------------------------------------------
# File Name: 47_merge.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Merge Sort. Divide and conquer; merges sorted halves. O(n log n). Stable.
# -------------------------------------------------

def merge_sort(items):
    """Divide and conquer: divide, sort halves, merge."""
    if len(items) <= 1:
        return items.copy()  # Base case: list of 0-1 elements
    mid = len(items) // 2
    left = merge_sort(items[:mid])   # Sort left half
    right = merge_sort(items[mid:])     # Sort right half
    return merge(left, right)        # Merge both halves


def merge(left, right):
    """Merges two sorted lists into one sorted list."""
    result = []
    i = j = 0
    # Compare and take the smaller from each list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample)
    print("Merge Sort:", merge_sort(sample))
