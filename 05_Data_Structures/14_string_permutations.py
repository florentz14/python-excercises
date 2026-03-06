# -------------------------------------------------
# File: 14_string_permutations.py (String Permutations)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - String Algorithms
#
# Description:
#   Generates all permutations of a string recursively.
#   For each position, pick a character and recurse on the rest.
#
# Complexity: O(n!).
# -------------------------------------------------


def permutations(s):
    """Returns all permutations of string s (recursive)."""
    if len(s) <= 1:
        return [s]

    result = []
    for i, char in enumerate(s):
        rest = s[:i] + s[i + 1:]
        for perm in permutations(rest):
            result.append(char + perm)
    return result


if __name__ == "__main__":
    print("=== String Algorithms: Permutations ===\n")

    s = "abc"
    print(f"Permutations of '{s}': {permutations(s)}")
