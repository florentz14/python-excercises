"""
05_Estructuras_de_Datos - Búsqueda de patrón en texto (fuerza bruta)
=====================================================================
Complejidad: O(n*m). n=len(texto), m=len(patron).
"""


def busqueda_bruta_texto(texto, patron):
    """Primera ocurrencia del patrón en el texto. -1 si no existe."""
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
    """Lista de índices de todas las ocurrencias del patrón."""
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
