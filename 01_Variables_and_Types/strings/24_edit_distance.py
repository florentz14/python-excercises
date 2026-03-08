# -------------------------------------------------
# File Name: 24_edit_distance.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Levenshtein edit distance between two strings.
# -------------------------------------------------

def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
    return dp[m][n]

def main():
    print(edit_distance("horse", "ros"))
    print(edit_distance("intention", "execution"))

if __name__ == "__main__":
    main()
