# -------------------------------------------------
# File Name: 12_group_anagrams.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Group anagrams together using sorted tuple as key.
# -------------------------------------------------

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))
