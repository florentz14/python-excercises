# -------------------------------------------------
# File Name: 49_heap.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Heap Sort. Builds max-heap, repeatedly extracts max. O(n log n). In-place.
# -------------------------------------------------

def heap_sort(arr):
    """Sorts by building max-heap and repeatedly extracting max."""
    arr = arr.copy()
    n = len(arr)
    # Build max-heap from bottom up (start at last non-leaf)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract max, swap to end, re-heapify
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    """Sinks element at i so subtree rooted at i is a max-heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


if __name__ == "__main__":
    print("=== Sorting: Heap Sort ===\n")

    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Heap Sort:", heap_sort(arr))
