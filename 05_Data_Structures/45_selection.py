# -------------------------------------------------
# File Name: 45_selection.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Selection Sort. Repeatedly selects minimum and places at front. O(n²).
# -------------------------------------------------

def selection_sort(items):
    """At each step places the minimum of the rest at the current position."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        min_idx = i  # Assume the minimum is at the current position
        # Find the minimum in the unsorted subarray
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j  # Update minimum index
        # Swap the minimum with the current position
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample)
    print("Selection Sort:", selection_sort(sample))
