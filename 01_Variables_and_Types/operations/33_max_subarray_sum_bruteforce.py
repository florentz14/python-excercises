"""
Maximum Sum Subarray - Brute force version
==========================================
Topic: Operations (01_Variables_and_Types/operations)
Description: Find the maximum sum of any subarray of size k. Brute force approach:
for each possible window of size k, calculate the sum from scratch.

Input:  First line: space-separated numbers
        Second line: window size k
Output: Maximum sum of any subarray of size k

Complexity:
    Time:   O(n * k) - For each of (n - k + 1) windows, we sum k elements
    Space:  O(1)
"""


def subarray_sum_bruteforce(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of size k.
    Recomputes each window sum from scratch.
    """
    largest = float("-inf")

    for start in range(len(nums) - k + 1):
        window_sum = 0
        for i in range(start, start + k):
            window_sum += nums[i]
        largest = max(largest, window_sum)

    return largest


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    result = subarray_sum_bruteforce(nums, k)
    print(result)
