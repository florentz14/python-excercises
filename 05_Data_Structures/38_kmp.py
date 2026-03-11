# -------------------------------------------------
# File Name: 38_kmp.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: KMP algorithm for pattern matching. Builds failure table for linear-time search. O(n+m).
# -------------------------------------------------

def construir_tabla_lps(pattern):
    """LPS table: Longest Proper Prefix which is also Suffix."""
    m = len(pattern)
    lps = [0] * m  # lps[i] = length of longest proper prefix that is also suffix
    length = 0   # Length of previous prefix
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length  # Match → extend prefix
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Back up in LPS table
            else:
                lps[i] = 0  # No matching prefix
                i += 1
    return lps


def kmp_busqueda(text, pattern):
    """First occurrence of the pattern with KMP. -1 if not found."""
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    lps = construir_tabla_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        if i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def kmp_busqueda_todas(text, pattern):
    """All occurrences of the pattern with KMP."""
    n, m = len(text), len(pattern)
    occurrences = []
    if m == 0:
        return [0]
    if m > n:
        return []
    lps = construir_tabla_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences


if __name__ == "__main__":
    text = "ABABDABACDABABCABCABAB"
    pattern = "ABABCABAB"
    print("Text:", repr(text), "Pattern:", repr(pattern))
    print("KMP first occurrence:", kmp_busqueda(text, pattern))
    print("KMP todas:", kmp_busqueda_todas(text, pattern))
