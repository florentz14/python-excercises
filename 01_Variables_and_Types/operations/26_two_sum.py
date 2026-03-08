# -------------------------------------------------
# File Name: 26_two_sum.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Two Sum: finds two indices that add up to the target.
# -------------------------------------------------

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
