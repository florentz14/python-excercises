"""
Two Sum - Find two indices that add up to the target
====================================================
Topic: Operations (01_Variables_and_Types/operations)
Description: Given an array of integers and a target value, finds the indices
of two numbers that sum exactly to the target. Uses a single pass with a
dictionary for O(1) lookup.

Input:  One line with space-separated numbers (the array).
        A second line with the target value.
Output: The two indices separated by space, or empty if no solution exists.

Complexity:
    - Time:   O(n) where n is the array size.
      A single loop traverses the array; each lookup and storage
      in the dictionary is O(1) on average.
    - Space:  O(n) in the worst case, for the dictionary that may
      store up to n pairs (value -> index).
"""


def two_sum(arr: list[int], target: int) -> list[int]:
    """
    Finds two indices whose values sum to target.
    Uses hash map for O(1) complement lookup.
    """
    # Dictionary: value already seen -> index where it was seen
    num_to_index = {}

    for i, num in enumerate(arr):
        # Complement: the value we need so that num + complement = target
        complement = target - num

        # If we already saw the complement, return both indices
        if complement in num_to_index:
            return [num_to_index[complement], i]

        # Store the current value and its index for future lookups
        num_to_index[num] = i

    # No pair was found that sums to target
    return []


if __name__ == "__main__":
    # Read array: space-separated numbers
    arr = [int(x) for x in input().split()]
    # Read target
    target = int(input())

    res = two_sum(arr, target)
    # Print indices separated by space (or empty string if no solution)
    print(" ".join(map(str, res)))
