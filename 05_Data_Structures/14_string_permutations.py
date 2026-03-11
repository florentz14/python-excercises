# -------------------------------------------------
# File Name: 14_string_permutations.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: String permutation generation. All permutations of a string using backtracking.
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
