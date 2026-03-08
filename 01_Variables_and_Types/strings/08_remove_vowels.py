# -------------------------------------------------
# File Name: 08_remove_vowels.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Remove vowels from string (a, e, i, o, u case-insensitive).
# -------------------------------------------------

VOWELS = set("aeiouAEIOU")

def remove_vowels(s: str) -> str:
    return "".join(c for c in s if c not in VOWELS)

if __name__ == "__main__":
    s = "hello world"
    print("Original:", s)
    print("Without vowels:", remove_vowels(s))
