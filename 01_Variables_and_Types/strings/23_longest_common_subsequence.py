# -------------------------------------------------
# File Name: 23_longest_common_subsequence.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Longest common subsequence (LCS) via dynamic programming.
# -------------------------------------------------

def lcs(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def main():
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))

if __name__ == "__main__":
    main()
