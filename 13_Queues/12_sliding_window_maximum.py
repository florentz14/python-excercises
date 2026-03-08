# -------------------------------------------------
# File Name: 12_sliding_window_maximum.py
# Author: Florentino Báez
# Date: 13_Queues
# Description: Sliding window maximum. Monotonic deque. O(n).
# -------------------------------------------------

from collections import deque


def max_sliding_window(nums, k):
    """
    O(n) time using monotonic decreasing deque.
    """
    result = []
    dq = deque()  # indices, values decreasing

    for i, num in enumerate(nums):
        # Remove expired indices (outside window)
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing: remove elements smaller than current
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print("=" * 55)
    print("Sliding Window Maximum")
    print("=" * 55)

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    result = max_sliding_window(nums, k)
    print(f"nums = {nums}")
    print(f"k = {k}")
    print(f"Output: {result}")
    print()
    print("Windows:")
    for i in range(len(nums) - k + 1):
        window = nums[i : i + k]
        print(f"  [{i}:{i+k}] {window} -> max = {result[i]}")
