# -------------------------------------------------
# File Name: 30_two_sum_v2.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Two Sum (v2) - Compact implementation using dictionary lookup.
# -------------------------------------------------

def two_sum(arr: list[int], target: int) -> list[int]:
    """Finds two indices whose values sum to target. Optimized single-pass."""
    s: dict[int, int] = {} # dictionary to store the numbers and their indices
    # enumerate is a function that returns the index and the value of the element in the array
    for i, num in enumerate(arr):
        if target - num in s: # if the complement of the number is in the dictionary
            return [s[target - num], i] # return the indices of the two numbers
        s[num] = i # add the number and its index to the dictionary
    return [] # if no solution is found, return an empty list


if __name__ == "__main__":
    arr = [int(x) for x in input().split()] # input the array
    target = int(input()) # target is the sum of the two numbers
    res = two_sum(arr, target) # call the function to find the two numbers
    print(" ".join(map(str, res))) # print the indices of the two numbers
