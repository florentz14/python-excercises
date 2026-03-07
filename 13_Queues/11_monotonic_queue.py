"""
13_Queues - Monotonic Queue
============================
Deque that maintains monotonic order (increasing or decreasing).
Used for: Sliding Window Maximum, Sliding Window Minimum.

Key idea: before adding new element, remove elements that break monotonicity.
"""

from collections import deque


def max_sliding_window(nums, k):
    """
    Sliding Window Maximum using monotonic decreasing queue.
    Queue stores indices; values at those indices are in decreasing order.
    """
    result = []
    dq = deque()  # indices

    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Maintain decreasing order: remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def min_sliding_window(nums, k):
    """Sliding Window Minimum using monotonic increasing queue."""
    result = []
    dq = deque()

    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] > num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print("=" * 55)
    print("Monotonic Queue - Sliding Window")
    print("=" * 55)

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    max_result = max_sliding_window(nums, k)
    min_result = min_sliding_window(nums, k)

    print(f"nums = {nums}, k = {k}")
    print(f"Sliding Window Maximum: {max_result}")
    print(f"Sliding Window Minimum: {min_result}")
