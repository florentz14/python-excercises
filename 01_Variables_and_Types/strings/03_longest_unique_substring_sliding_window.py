# -------------------------------------------------
# File Name: 03_longest_unique_substring_sliding_window.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest substring without repeating chars - sliding window.
# -------------------------------------------------

def longest_unique_substring_optimized(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    Sliding window: expand with right, shrink with left when duplicate found.
    """
    left = 0
    longest = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    text = input().strip()
    result = longest_unique_substring_optimized(text)
    print(result)
