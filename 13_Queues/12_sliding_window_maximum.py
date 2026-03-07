"""
13_Queues - Sliding Window Maximum (LeetCode 239)
==================================================
Classic problem using monotonic queue.

Given: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Each element is the max of the current window of size k.
"""

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
