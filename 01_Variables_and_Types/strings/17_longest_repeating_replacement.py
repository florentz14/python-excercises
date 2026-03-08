# -------------------------------------------------
# File Name: 17_longest_repeating_replacement.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest substring with at most k character replacements.
# -------------------------------------------------

from collections import Counter

def longest_repeating_replacement(s: str, k: int) -> int:
    left = 0
    max_freq = 0
    freq = Counter()
    for right, c in enumerate(s):
        freq[c] += 1
        max_freq = max(max_freq, freq[c])
        if right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1
    return len(s) - left

def main():
    s, k = "AABABBA", 1
    print(longest_repeating_replacement(s, k))

if __name__ == "__main__":
    main()
