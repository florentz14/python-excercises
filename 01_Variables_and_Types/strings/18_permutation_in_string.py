# -------------------------------------------------
# File Name: 18_permutation_in_string.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Check if permutation of s1 exists in s2.
# -------------------------------------------------

from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    target = Counter(s1)
    window = Counter(s2[:len(s1)])
    for i in range(len(s1), len(s2)):
        if window == target:
            return True
        window[s2[i]] += 1
        c = s2[i - len(s1)]
        window[c] -= 1
        if window[c] == 0:
            del window[c]
    return window == target

def main():
    print(check_inclusion("ab", "eidbaooo"))
    print(check_inclusion("ab", "eidboaoo"))

if __name__ == "__main__":
    main()
