# -------------------------------------------------
# File Name: 38_kmp.py
# Author: Florentino Báez
# Date: Data Structures - Search Algorithms
# Description: KMP Algorithm (Knuth-Morris-Pratt).
#              Pattern search in text that avoids re-comparing
#              characters already verified. Pre-processes the pattern
#              by building the LPS table (Longest Proper Prefix
#              which is also Suffix) to skip positions.
#              Complexity: O(n + m) in time, O(m) in space.
# -------------------------------------------------


def construir_tabla_lps(patron):
    """LPS table: Longest Proper Prefix which is also Suffix."""
    m = len(patron)
    lps = [0] * m  # lps[i] = length of longest proper prefix that is also suffix
    longitud = 0   # Length of previous prefix
    i = 1
    while i < m:
        if patron[i] == patron[longitud]:
            longitud += 1
            lps[i] = longitud  # Match → extend prefix
            i += 1
        else:
            if longitud != 0:
                longitud = lps[longitud - 1]  # Back up in LPS table
            else:
                lps[i] = 0  # No matching prefix
                i += 1
    return lps


def kmp_busqueda(texto, patron):
    """First occurrence of the pattern with KMP. -1 if not found."""
    n, m = len(texto), len(patron)
    if m == 0:
        return 0
    if m > n:
        return -1
    lps = construir_tabla_lps(patron)
    i = j = 0
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        if i < n and texto[i] != patron[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def kmp_busqueda_todas(texto, patron):
    """All occurrences of the pattern with KMP."""
    n, m = len(texto), len(patron)
    ocurrencias = []
    if m == 0:
        return [0]
    if m > n:
        return []
    lps = construir_tabla_lps(patron)
    i = j = 0
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
        if j == m:
            ocurrencias.append(i - j)
            j = lps[j - 1]
        elif i < n and texto[i] != patron[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ocurrencias


if __name__ == "__main__":
    texto = "ABABDABACDABABCABCABAB"
    patron = "ABABCABAB"
    print("Texto:", repr(texto), "Patrón:", repr(patron))
    print("KMP primera ocurrencia:", kmp_busqueda(texto, patron))
    print("KMP todas:", kmp_busqueda_todas(texto, patron))
