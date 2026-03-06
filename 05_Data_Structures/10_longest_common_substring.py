# -------------------------------------------------
# File Name: 10_longest_common_substring.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Longest Common Substring.
#              Uses dynamic programming with a 2D table where
#              dp[i][j] stores the length of the common substring
#              ending at X[i-1] and Y[j-1]. Tracks the position
#              and maximum length to extract the substring.
#              Complexity: O(m * n) in time and space.
# -------------------------------------------------

print("=== 3. Subcadena Común Más Larga ===\n")


def longest_common_substring(X, Y):
    """
    Finds the longest common substring between two strings.
    Complexity: O(m * n)
    """
    m, n = len(X), len(Y)
    # DP table: dp[i][j] = length of common substring ending at X[i-1], Y[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    longitud_maxima = 0   # Length of the longest substring found
    posicion_maxima = 0   # End position in X of the longest substring

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                # Characters match: extend the previous substring
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longitud_maxima:
                    longitud_maxima = dp[i][j]  # Update maximum
                    posicion_maxima = i          # Save end position

    # Extract the substring from the recorded position
    subcadena = X[posicion_maxima - longitud_maxima:posicion_maxima]
    return longitud_maxima, subcadena


if __name__ == "__main__":
    str1_lcs = "ABCDGH"
    str2_lcs = "ACDGHR"

    print(f"String 1: '{str1_lcs}'")
    print(f"String 2: '{str2_lcs}'")
    longitud, subcadena = longest_common_substring(str1_lcs, str2_lcs)
    print(f"Longitud: {longitud}")
    print(f"Subcadena: '{subcadena}'")
