# ------------------------------------------------------------
# Algorithm: Kadane's Algorithm
# Purpose:
#   Find the maximum sum of a contiguous subarray.
# Return:
#   Maximum subarray sum.
# Complexity:
#   Time  : O(n)
#   Space : O(1)
# ------------------------------------------------------------
# Author: Florentino Báez
# ------------------------------------------------------------


def max_subarray_sum(nums: list[int]) -> int:
    # Initialize current and best sums with the first element
    current_sum = best_sum = nums[0]

    # Process the rest of the array
    for num in nums[1:]:
        # Either start a new subarray or extend the current one
        current_sum = max(num, current_sum + num)

        # Update the best sum found so far
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    print("=== Kadane: Maximum Subarray Sum ===\n")

    examples = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3],
    ]
    for arr in examples:
        print(f"Array: {arr}")
        print(f"  Max subarray sum: {max_subarray_sum(arr)}")
