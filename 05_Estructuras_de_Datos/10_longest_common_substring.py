# Archivo: 44_03_longest_common_substring.py
# Descripción: Subcadena común más larga (Longest Common Substring)

print("=== 3. Subcadena Común Más Larga ===\n")


def longest_common_substring(X, Y):
    """
    Encuentra la subcadena común más larga entre dos strings.
    Complejidad: O(m * n)
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    longitud_maxima = 0
    posicion_maxima = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longitud_maxima:
                    longitud_maxima = dp[i][j]
                    posicion_maxima = i

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
