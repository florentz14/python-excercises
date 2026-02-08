# -------------------------------------------------
# File Name: 11_edit_distance.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Edit Distance (Levenshtein).
#              Computes the minimum number of operations (insert,
#              delete, substitute) to transform one string into
#              another. Uses dynamic programming with table dp
#              where dp[i][j] = distance between str1[:i] and str2[:j].
#              Complexity: O(m * n) in time and space.
# -------------------------------------------------

print("=== 4. Distancia de Edición (Levenshtein) ===\n")


def edit_distance(str1, str2):
    """
    Edit distance (Levenshtein): minimum number of operations
    (insert, delete, substitute) to transform str1 into str2.
    Complexity: O(m * n)
    """
    m, n = len(str1), len(str2)
    # DP table: dp[i][j] = edit distance between str1[:i] and str2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: transforming empty string into str1[:i] requires i deletions
    for i in range(m + 1):
        dp[i][0] = i
    # Base case: transforming empty string into str2[:j] requires j insertions
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Same characters: no cost
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete character from str1
                    dp[i][j - 1],      # Insert character into str1
                    dp[i - 1][j - 1]   # Substitute character
                )

    return dp[m][n]  # Distance between the complete strings


if __name__ == "__main__":
    palabra1 = "kitten"
    palabra2 = "sitting"

    print(f"Palabra 1: '{palabra1}'")
    print(f"Palabra 2: '{palabra2}'")
    distancia = edit_distance(palabra1, palabra2)
    print(f"Distancia de edición: {distancia}")
    print(f"Operaciones necesarias para convertir '{palabra1}' en '{palabra2}'")
