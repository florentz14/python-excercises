# -------------------------------------------------
# File Name: 12_longest_palindromic_substring.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Longest palindromic substring. Expands around centers or uses DP. Finds the longest substring that reads the same forwards and backwards.
# -------------------------------------------------

print("=== 5. Longest Palindromic Substring ===\n")


def longest_palindromic_substring(s):
    """
    Longest palindromic substring (expansion from center).
    Complexity: O(n²)
    """
    if not s:
        return ""

    def expandir_desde_centro(left, right):
        """Expands while the ends match (it is a palindrome)."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1   # Expand to the left
            right += 1     # Expand to the right
        return s[left + 1:right]  # Palindromic substring found

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
    print(f"Longest palindromic substring: '{palindromo_max}'")
