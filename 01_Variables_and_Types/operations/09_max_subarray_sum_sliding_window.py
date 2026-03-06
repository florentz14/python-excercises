"""
Maximum Sum Subarray - Sliding window version
=============================================
Topic: Operations (01_Variables_and_Types/operations)
Description: Find the maximum sum of a subarray of size k using the sliding
window technique. Instead of recomputing each subarray sum, update the window
sum incrementally: new_sum = prev_sum - element_left + element_entered.

Input:  First line: space-separated numbers
        Second line: window size k
Output: Maximum sum of any subarray of size k

Complexity:
    Time:   O(n) - Single pass, O(1) work per step
    Space:  O(1)
"""


def subarray_sum_fixed(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of a subarray of size k using sliding window.
    Updates window sum incrementally instead of recomputing.
    """
    # Step 1: Compute the first window sum
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]

    largest = window_sum

    # Step 2: Slide the window across the array
    for right in range(k, len(nums)):
        left = right - k  # Element leaving the window
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)

    return largest


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
