# ------------------------------------------------------------
# File: 11_anagram_check.py
# Purpose: Check if two strings are anagrams.
# Description: Same chars, same count. Use sorted() or Counter.
# ------------------------------------------------------------

from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2) or Counter(s1) == Counter(s2)

def main():
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))

if __name__ == "__main__":
    main()
