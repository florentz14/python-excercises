# -------------------------------------------------
# File Name: 10_longest_common_substring.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Longest Common Substring via dynamic programming. dp[i][j] = length of common substring ending at X[i-1], Y[j-1]. O(m*n).
# -------------------------------------------------

def longest_common_substring(X, Y):
    """
    Finds the longest common substring between two strings.
    Complexity: O(m * n)
    """
    m, n = len(X), len(Y)
    # DP table: dp[i][j] = length of common substring ending at X[i-1], Y[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_len = 0
    max_pos = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_pos = i

    substring = X[max_pos - max_len:max_pos]
    return max_len, substring


if __name__ == "__main__":
    print("=== String Algorithms: Longest Common Substring ===\n")

    s1, s2 = "ABCDGH", "ACDGHR"
    print(f"String 1: '{s1}'")
    print(f"String 2: '{s2}'")
    length, substr = longest_common_substring(s1, s2)
    print(f"Length: {length}")
    print(f"Substring: '{substr}'")
