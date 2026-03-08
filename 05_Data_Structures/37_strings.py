# -------------------------------------------------
# File Name: 37_strings.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: String algorithms collection. Pattern matching and string utilities.
# -------------------------------------------------

def busqueda_bruta_texto(texto, patron):
    """First occurrence of the pattern in the text. -1 if not found."""
    n, m = len(texto), len(patron)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        j = 0
        while j < m and texto[i + j] == patron[j]:
            j += 1
        if j == m:
            return i
    return -1


def busqueda_bruta_todas(texto, patron):
    """List of indices of all occurrences of the pattern."""
    n, m = len(texto), len(patron)
    ocurrencias = []
    if m == 0:
        return [0]
    if m > n:
        return []
    for i in range(n - m + 1):
        j = 0
        while j < m and texto[i + j] == patron[j]:
            j += 1
        if j == m:
            ocurrencias.append(i)
    return ocurrencias


if __name__ == "__main__":
    texto = "abracadabra"
    patron = "abra"
    print("Texto:", repr(texto), "Patrón:", repr(patron))
    print("Primera ocurrencia:", busqueda_bruta_texto(texto, patron))
    print("Todas las ocurrencias:", busqueda_bruta_todas(texto, patron))
