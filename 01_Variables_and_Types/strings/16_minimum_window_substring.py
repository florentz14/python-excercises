# -------------------------------------------------
# File Name: 16_minimum_window_substring.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Minimum window substring containing all chars of pattern.
# -------------------------------------------------

from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    need = Counter(t)
    have = 0
    required = len(need)
    freq = {}
    left = 0
    result = (float("inf"), 0, 0)
    for right, c in enumerate(s):
        freq[c] = freq.get(c, 0) + 1
        if c in need and freq[c] == need[c]:
            have += 1
        while have == required:
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            freq[s[left]] -= 1
            if s[left] in need and freq[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    return s[result[1]:result[2] + 1] if result[0] != float("inf") else ""

def main():
    s, t = "ADOBECODEBANC", "ABC"
    print(min_window(s, t))

if __name__ == "__main__":
    main()
