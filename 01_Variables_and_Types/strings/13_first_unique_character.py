# ------------------------------------------------------------
# File: 13_first_unique_character.py
# Purpose: First non-repeating character.
# Description: Two passes: count, then find first with count 1.
# ------------------------------------------------------------

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
