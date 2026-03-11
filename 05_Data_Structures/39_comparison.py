# -------------------------------------------------
# File Name: 39_comparison.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Search algorithm comparison. Measures linear vs binary vs KMP performance.
# -------------------------------------------------

import time


# === Linear Search ===
def busqueda_lineal(items, target):
    """Searches element by element. Returns index or -1."""
    for index, elemento in enumerate(items):
        if elemento == target:
            return index
    return -1


# === Binary Search ===
def busqueda_binaria(items, target):
    """Iterative binary search. Returns index or -1."""
    if not items:
        return -1
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# === Pattern Search (Brute Force) ===
def busqueda_bruta_texto(text, pattern):
    """First occurrence of pattern in text. Returns -1 if not found."""
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


# === KMP Algorithm ===
def construir_tabla_lps(pattern):
    """Tabla LPS: Longest Proper Prefix which is also Suffix."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_busqueda(text, pattern):
    """First occurrence of pattern with KMP. Returns -1 if not found."""
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


# === Comparisons ===
def comparar_busquedas_lista(items, target, ordenada=False):
    """Compare linear search vs binary search."""
    if ordenada:
        items = sorted(items)
    print(f"\nSearching for {target} in list with {len(items)} elements ({'sorted' if ordenada else 'unsorted'}):")
    start = time.time()
    res_lineal = busqueda_lineal(items, target)
    tiempo_lineal = time.time() - start
    print(f"  Linear: {tiempo_lineal*1000:.4f} ms (index: {res_lineal})")
    if ordenada:
        start = time.time()
        res_bin = busqueda_binaria(items, target)
        tiempo_bin = time.time() - start
        print(f"  Binary: {tiempo_bin*1000:.4f} ms (index: {res_bin})")
        if tiempo_bin > 0:
            print(f"  Speedup: {tiempo_lineal/tiempo_bin:.2f}x faster")
    else:
        print("  (Binary search requires a sorted list)")


def comparar_busquedas_texto(text, pattern):
    """Compare brute-force search vs KMP."""
    print(f"\nBuscando {repr(pattern)} en text de {len(text)} caracteres:")
    start = time.time()
    res_bruta = busqueda_bruta_texto(text, pattern)
    tiempo_bruta = time.time() - start
    start = time.time()
    res_kmp = kmp_busqueda(text, pattern)
    tiempo_kmp = time.time() - start
    print(f"  Brute force: {tiempo_bruta*1000:.4f} ms (index: {res_bruta})")
    print(f"  KMP: {tiempo_kmp*1000:.4f} ms (index: {res_kmp})")
    if tiempo_kmp > 0:
        print(f"  Speedup: {tiempo_bruta/tiempo_kmp:.2f}x faster")


if __name__ == "__main__":
    print("=== Search Algorithm Comparison ===\n")
    for tam in [100, 1000, 10000]:
        items = list(range(tam))
        comparar_busquedas_lista(items, tam // 2, ordenada=True)
    texto_largo = "AB" * 1000 + "CD" * 1000
    patron_largo = "ABCD" * 10
    comparar_busquedas_texto(texto_largo, patron_largo)
