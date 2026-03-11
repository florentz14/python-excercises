# -------------------------------------------------
# File Name: 48_quick.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Quick Sort. Pivot partition, recursive sort. O(n log n) avg, O(n²) worst. In-place.
# -------------------------------------------------

def quick_sort(items):
    """Version that uses auxiliary lists (clear). Pivot: middle element."""
    if len(items) <= 1:
        return items.copy()
    pivot = items[len(items) // 2]                 # Choose middle pivot
    lower = [x for x in items if x < pivot]        # Smaller elements
    equal = [x for x in items if x == pivot]       # Equal elements
    greater = [x for x in items if x > pivot]      # Larger elements
    return quick_sort(lower) + equal + quick_sort(greater)


def quick_sort_inplace(items, start=0, end=None):
    """Quick sort in-place (modifies the list)."""
    if end is None:
        end = len(items) - 1
    if start < end:
        pivot_idx = partition(items, start, end)             # Partition
        quick_sort_inplace(items, start, pivot_idx - 1)      # Sort left
        quick_sort_inplace(items, pivot_idx + 1, end)        # Sort right
    return items


def partition(items, start, end):
    """Partitions around the pivot (last element) - Lomuto scheme."""
    pivot = items[end]            # Pivot = last element
    i = start - 1                # Index of last smaller element
    for j in range(start, end):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]  # Move smaller to the left
    items[i + 1], items[end] = items[end], items[i + 1]  # Place pivot in position
    return i + 1  # Final pivot position


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Quick Sort:", quick_sort(arr))
    copy_arr = arr.copy()
    quick_sort_inplace(copy_arr)
    print("Quick Sort In-place:", copy_arr)


# Backward-compatible alias.
particionar = partition
