# -------------------------------------------------
# File Name: 02_longest_unique_substring_bruteforce.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest substring without repeating characters - brute force.
# -------------------------------------------------

def longest_unique_substring_bruteforce(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    Tries every starting position and expands until a duplicate is found.
    """
    longest = 0

    for start in range(len(s)):
        seen = set()
        for end in range(start, len(s)):
            if s[end] in seen:
                break
            seen.add(s[end])
            longest = max(longest, end - start + 1)

    return longest


if __name__ == "__main__":
    text = input().strip()
    result = longest_unique_substring_bruteforce(text)
    print(result)
