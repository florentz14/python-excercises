# -------------------------------------------------
# File Name: 28_string_permutations.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Generate all permutations via itertools or backtracking.
# -------------------------------------------------

import itertools

def permutations_itertools(s: str) -> list[str]:
    return ["".join(p) for p in itertools.permutations(s)]

def permutations_backtrack(s: str) -> list[str]:
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append("".join(path))
            return
        for i, c in enumerate(remaining):
            backtrack(path + [c], remaining[:i] + remaining[i+1:])
    backtrack([], list(s))
    return result

def main():
    s = "abc"
    print(permutations_itertools(s))
    print(permutations_backtrack(s))

if __name__ == "__main__":
    main()
