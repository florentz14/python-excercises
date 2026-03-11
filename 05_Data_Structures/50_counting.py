# -------------------------------------------------
# File Name: 50_counting.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Counting Sort. Non-comparison sort for small integer range. O(n+k).
# -------------------------------------------------

def counting_sort(items, maximum=None):
    """Sorts by counting occurrences of each value (non-negative integers)."""
    if maximum is None:
        maximum = max(items) if items else 0
    count = [0] * (maximum + 1)  # Count array for each possible value
    for num in items:
        count[num] += 1         # Count each occurrence
    result = []
    for i in range(maximum + 1):
        result.extend([i] * count[i])  # Rebuild sorted list
    return result


if __name__ == "__main__":
    sample = [4, 2, 2, 8, 3, 3, 1]
    print("Original list:", sample)
    print("Counting Sort:", counting_sort(sample))
