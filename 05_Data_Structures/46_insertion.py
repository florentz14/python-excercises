# -------------------------------------------------
# File Name: 46_insertion.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Insertion Sort. Builds sorted prefix by inserting each element. O(n²). Stable.
# -------------------------------------------------

def insertion_sort(items):
    """Inserts each element into its place within the already sorted portion."""
    items = items.copy()
    for i in range(1, len(items)):
        key = items[i]  # Element to insert
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key  # Insert key at its correct position
    return items


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Insertion Sort:", insertion_sort(arr))
