# -------------------------------------------------
# File Name: 25_palindrome_partitioning.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Return list of all palindrome partitions via backtracking.
# -------------------------------------------------

def partition(s: str) -> list[list[str]]:
    result: list[list[str]] = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, path: list[str]) -> None:
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result

def main() -> None:
    s = "aab"
    print(partition(s))

if __name__ == "__main__":
    main()
