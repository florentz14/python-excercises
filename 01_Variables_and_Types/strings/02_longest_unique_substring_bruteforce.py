"""
Longest Substring Without Repeating Characters - Brute force version
===================================================================
Topic: Strings (01_Variables_and_Types/strings)
Description: Find the length of the longest substring without repeating characters.
For each starting position, expand to the right until a repeated character is found.

Input:  A string (e.g. "abccabcabcc")
Output: Length of longest unique substring (e.g. 3)

Complexity:
    Time:   O(n²) - For each start, potentially scan to end
    Space:  O(n)  - Set to track characters
"""


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
