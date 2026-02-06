"""
05_Estructuras_de_Datos - Comparación de eficiencia (lineal vs binaria, bruta vs KMP)
======================================================================================
"""

import time

from busqueda_00_lineal import busqueda_lineal
from busqueda_01_binaria import busqueda_binaria
from busqueda_02_strings import busqueda_bruta_texto
from busqueda_03_kmp import kmp_busqueda


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
