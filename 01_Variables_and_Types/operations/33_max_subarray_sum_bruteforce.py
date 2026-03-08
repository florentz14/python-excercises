# -------------------------------------------------
# File Name: 33_max_subarray_sum_bruteforce.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Maximum sum of fixed-size subarray using brute force.
# -------------------------------------------------

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
