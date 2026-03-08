# -------------------------------------------------
# File Name: 05_longest_unique_substring_freq_counter.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest substring without repeating chars - frequency counter.
# -------------------------------------------------

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
