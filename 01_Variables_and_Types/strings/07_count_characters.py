# -------------------------------------------------
# File Name: 07_count_characters.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Count character frequencies using Counter or dict.
# -------------------------------------------------

from collections import Counter

def count_chars(s: str) -> dict:
    return dict(Counter(s))

def count_chars_manual(s: str) -> dict:
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

if __name__ == "__main__":
    s = "banana"
    print("String:", s)
    print("Count (Counter):", count_chars(s))
    print("Count (manual):", count_chars_manual(s))
