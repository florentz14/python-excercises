# -------------------------------------------------
# File Name: 14_longest_palindromic_substring.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest palindromic substring via expand-around-center.
# -------------------------------------------------

def expand(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]

def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    best = s[0]
    for i in range(len(s)):
        odd = expand(s, i, i)
        even = expand(s, i, i + 1)
        best = max([best, odd, even], key=len)
    return best

if __name__ == "__main__":
    print(longest_palindrome("babad"))  # "bab" or "aba"
    print(longest_palindrome("cbbd"))   # "bb"
