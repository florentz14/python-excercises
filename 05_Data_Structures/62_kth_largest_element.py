# -------------------------------------------------
# File Name: 62_kth_largest_element.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Kth Largest Element (LeetCode 215). Min-heap of size k or QuickSelect. O(n log k).
# -------------------------------------------------

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Return the kth largest element. Use min-heap of size k.
    The root is the kth largest when we keep only the k largest.
    """
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def find_kth_largest_nlargest(nums: list[int], k: int) -> int:
    """Alternative: heapq.nlargest(k, nums)[-1]"""
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print("Kth Largest (k=2):", find_kth_largest(nums[:], k))  # 5
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print("Kth Largest (k=4):", find_kth_largest(nums2[:], k2))  # 4
