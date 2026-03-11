# -------------------------------------------------
# File Name: 37_strings.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: String algorithms collection. Pattern matching and string utilities.
# -------------------------------------------------

def busqueda_bruta_texto(text, pattern):
    """First occurrence of the pattern in the text. -1 if not found."""
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


def busqueda_bruta_todas(text, pattern):
    """List of indices of all occurrences of the pattern."""
    n, m = len(text), len(pattern)
    occurrences = []
    if m == 0:
        return [0]
    if m > n:
        return []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)
    return occurrences


if __name__ == "__main__":
    text = "abracadabra"
    pattern = "abra"
    print("Text:", repr(text), "Pattern:", repr(pattern))
    print("First occurrence:", busqueda_bruta_texto(text, pattern))
    print("Todas las occurrences:", busqueda_bruta_todas(text, pattern))
