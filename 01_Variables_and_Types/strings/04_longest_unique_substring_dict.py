# -------------------------------------------------
# File Name: 04_longest_unique_substring_dict.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest substring without repeating chars - dictionary version.
# -------------------------------------------------

def longest_unique_substring_dict(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    Uses last_seen[char] to jump left in one step when duplicate found.
    """
    # Dictionary to store the last position of each character
    last_seen = {}

    # Left boundary of the current window
    left = 0

    # Maximum length found
    longest = 0

    for right, char in enumerate(s):
        # If the character was seen inside the current window,
        # move left to one position after its last occurrence
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        # Update last seen position of the character
        last_seen[char] = right

        # Update maximum window length
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    text = input().strip()
    result = longest_unique_substring_dict(text)
    print(result)
