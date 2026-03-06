"""
Longest Substring Without Repeating Characters - Frequency counter version
=========================================================================
Topic: Strings (01_Variables_and_Types/strings)
Description: Sliding window with a frequency counter (defaultdict). When a
character's count exceeds 1, shrink the window from the left.

Input:  A string (e.g. "abccabcabcc")
Output: Length of longest unique substring (e.g. 3)

Complexity:
    Time:   O(n) - Each character visited at most twice
    Space:  O(n)  - Frequency counter
"""

from collections import defaultdict


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    Uses a frequency counter to track characters in the current window.
    """
    longest = 0
    l = 0
    counter: dict[str, int] = defaultdict(int)

    for r in range(len(s)):
        counter[s[r]] += 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)

    return longest


if __name__ == "__main__":
    text = input().strip()
    result = longest_substring_without_repeating_characters(text)
    print(result)
