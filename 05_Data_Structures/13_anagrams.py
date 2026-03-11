# -------------------------------------------------
# File Name: 13_anagrams.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Anagram utilities. is_anagram checks if two strings have same characters; group_anagrams groups words that are anagrams. O(n*k log k).
# -------------------------------------------------

def is_anagram(s1, s2):
    """Returns True if s1 and s2 are anagrams (same letters, different order)."""
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def group_anagrams(words):
    """Groups words that are anagrams. Returns dict: sorted_key -> list of words."""
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups


if __name__ == "__main__":
    print("=== String Algorithms: Anagrams ===\n")

    a, b = "listen", "silent"
    print(f"'{a}' and '{b}' are anagrams: {is_anagram(a, b)}")

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"\nWords: {words}")
    groups = group_anagrams(words)
    print("Anagram groups:")
    for g in groups.values():
        print(f"  {g}")
