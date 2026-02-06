"""
05_Estructuras_de_Datos - Comparación de eficiencia (lineal vs binaria, bruta vs KMP)
======================================================================================
"""

import time


# === Búsqueda lineal ===
def busqueda_lineal(lista, objetivo):
    """Busca elemento por elemento. Devuelve índice o -1."""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1


# === Búsqueda binaria ===
def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria iterativa. Devuelve índice o -1."""
    if not lista:
        return -1
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


# === Búsqueda de patrón (fuerza bruta) ===
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


# === Algoritmo KMP ===
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


# === Comparaciones ===
def comparar_busquedas_lista(lista, objetivo, ordenada=False):
    """Compara búsqueda lineal vs binaria."""
    if ordenada:
        lista = sorted(lista)
    print(f"\nBuscando {objetivo} en lista de {len(lista)} elementos ({'ordenada' if ordenada else 'no ordenada'}):")
    inicio = time.time()
    res_lineal = busqueda_lineal(lista, objetivo)
    tiempo_lineal = time.time() - inicio
    print(f"  Lineal: {tiempo_lineal*1000:.4f} ms (indice: {res_lineal})")
    if ordenada:
        inicio = time.time()
        res_bin = busqueda_binaria(lista, objetivo)
        tiempo_bin = time.time() - inicio
        print(f"  Binaria: {tiempo_bin*1000:.4f} ms (indice: {res_bin})")
        if tiempo_bin > 0:
            print(f"  Mejora: {tiempo_lineal/tiempo_bin:.2f}x mas rapido")
    else:
        print("  (Binaria requiere lista ordenada)")


def comparar_busquedas_texto(texto, patron):
    """Compara fuerza bruta vs KMP."""
    print(f"\nBuscando {repr(patron)} en texto de {len(texto)} caracteres:")
    inicio = time.time()
    res_bruta = busqueda_bruta_texto(texto, patron)
    tiempo_bruta = time.time() - inicio
    inicio = time.time()
    res_kmp = kmp_busqueda(texto, patron)
    tiempo_kmp = time.time() - inicio
    print(f"  Fuerza bruta: {tiempo_bruta*1000:.4f} ms (indice: {res_bruta})")
    print(f"  KMP: {tiempo_kmp*1000:.4f} ms (indice: {res_kmp})")
    if tiempo_kmp > 0:
        print(f"  Mejora: {tiempo_bruta/tiempo_kmp:.2f}x mas rapido")


if __name__ == "__main__":
    print("=== Comparacion de busquedas ===\n")
    for tam in [100, 1000, 10000]:
        lista = list(range(tam))
        comparar_busquedas_lista(lista, tam // 2, ordenada=True)
    texto_largo = "AB" * 1000 + "CD" * 1000
    patron_largo = "ABCD" * 10
    comparar_busquedas_texto(texto_largo, patron_largo)
