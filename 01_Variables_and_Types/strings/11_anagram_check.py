# -------------------------------------------------
# File Name: 11_anagram_check.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Check if two strings are anagrams. Same chars, same count.
# -------------------------------------------------

from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2) or Counter(s1) == Counter(s2)

def main():
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))

if __name__ == "__main__":
    main()
