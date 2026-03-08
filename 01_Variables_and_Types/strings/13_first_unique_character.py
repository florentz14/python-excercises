# -------------------------------------------------
# File Name: 13_first_unique_character.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Find index of first non-repeating character.
# -------------------------------------------------

from collections import Counter

def first_unique(s: str) -> int:
    cnt = Counter(s)
    for i, c in enumerate(s):
        if cnt[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(first_unique("leetcode"))   # 0 ('l')
    print(first_unique("loveleetcode"))  # 2 ('v')
