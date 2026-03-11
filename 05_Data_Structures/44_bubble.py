# -------------------------------------------------
# File Name: 44_bubble.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Bubble Sort. Adjacent swaps, bubbles largest to end. O(n²). Stable. In-place.
# -------------------------------------------------

def bubble_sort(items):
    """Classic bubble sort. Does not modify the original list."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        # In each pass, the largest element "bubbles" to the end
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                # Swap out-of-order adjacent elements
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def bubble_sort_optimized(items):
    """Stops if no swaps occur (list already sorted)."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        swapped = False  # Flag to detect if any changes occurred
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break  # List already sorted → terminate early
    return items


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Bubble Sort:", bubble_sort(arr))
    print("Bubble Sort Optimized:", bubble_sort_optimized(arr))


# Backward-compatible alias.
bubble_sort_optimizado = bubble_sort_optimized
