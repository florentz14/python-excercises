"""
05_Estructuras_de_Datos - Algoritmo KMP (Knuth-Morris-Pratt)
=============================================================
Búsqueda de patrón en texto. Complejidad: O(n + m).
"""


def construir_tabla_lps(patron):
    """Tabla LPS: Longest Proper Prefix which is also Suffix."""
    m = len(patron)
    lps = [0] * m
    longitud = 0
    i = 1
    while i < m:
        if patron[i] == patron[longitud]:
            longitud += 1
            lps[i] = longitud
            i += 1
        else:
            if longitud != 0:
                longitud = lps[longitud - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_busqueda(texto, patron):
    """Primera ocurrencia del patrón con KMP. -1 si no existe."""
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
    """Todas las ocurrencias del patrón con KMP."""
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
