# -------------------------------------------------
# File Name: 12_longest_palindromic_substring.py
# Author: Florentino Báez
# Date: Data Structures - String Algorithms
# Description: Longest Palindromic Substring.
#              Finds the longest substring that reads the same
#              from left to right as from right to left.
#              Uses the expansion-from-center method: for each
#              position, expand in both directions while
#              characters match (odd and even length).
#              Complexity: O(n²) in time, O(1) in space.
# -------------------------------------------------

print("=== 5. Subcadena Palindrómica Más Larga ===\n")


def longest_palindromic_substring(s):
    """
    Longest palindromic substring (expansion from center).
    Complexity: O(n²)
    """
    if not s:
        return ""

    def expandir_desde_centro(izquierda, derecha):
        """Expands while the ends match (it is a palindrome)."""
        while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
            izquierda -= 1   # Expand to the left
            derecha += 1     # Expand to the right
        return s[izquierda + 1:derecha]  # Palindromic substring found

    subcadena_max = ""

    for i in range(len(s)):
        # Odd-length palindromes (center = single character)
        pal1 = expandir_desde_centro(i, i)
        # Even-length palindromes (center = between two characters)
        pal2 = expandir_desde_centro(i, i + 1)
        # Update the maximum found
        if len(pal1) > len(subcadena_max):
            subcadena_max = pal1
        if len(pal2) > len(subcadena_max):
            subcadena_max = pal2

    return subcadena_max


if __name__ == "__main__":
    cadena_pal = "babad"
    print(f"Cadena: '{cadena_pal}'")
    palindromo_max = longest_palindromic_substring(cadena_pal)
    print(f"Subcadena palindrómica más larga: '{palindromo_max}'")
