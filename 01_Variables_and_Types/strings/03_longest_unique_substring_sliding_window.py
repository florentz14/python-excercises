"""
Longest Substring Without Repeating Characters - Sliding window version
=======================================================================
Topic: Strings (01_Variables_and_Types/strings)
Description: Find the length of the longest substring without repeating characters.
Uses a sliding window with two pointers (left, right) and a set to track characters.

Input:  A string (e.g. "abccabcabcc")
Output: Length of longest unique substring (e.g. 3)

Complexity:
    Time:   O(n) - Each character visited at most twice (by left and right)
    Space:  O(n)  - Set for characters in window
"""


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
