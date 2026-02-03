"""
05_Estructuras_de_Datos - Comparación de métodos de ordenamiento
=================================================================
Mide tiempos de cada algoritmo sobre la misma lista.
"""

import time

from ordenamiento_00_utilidades import esta_ordenada, generar_lista_aleatoria
from ordenamiento_01_bubble import bubble_sort, bubble_sort_optimizado
from ordenamiento_02_selection import selection_sort
from ordenamiento_03_insertion import insertion_sort
from ordenamiento_04_merge import merge_sort
from ordenamiento_05_quick import quick_sort
from ordenamiento_06_heap import heap_sort
from ordenamiento_07_counting import counting_sort


def comparar_metodos_ordenamiento(lista, mostrar_resultados=True):
    """Compara tiempos de todos los métodos. No modifica la lista original."""
    metodos = {
        "Bubble Sort": bubble_sort,
        "Bubble Sort Optimizado": bubble_sort_optimizado,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Python sorted()": sorted,
    }
    tiempos = {}
    print(f"\nComparando métodos para lista de {len(lista)} elementos:")
    print("=" * 70)
    for nombre, metodo in metodos.items():
        lista_copia = lista.copy()
        inicio = time.time()
        try:
            resultado = metodo(lista_copia)
            tiempo = time.time() - inicio
            ordenada = esta_ordenada(resultado)
            tiempos[nombre] = tiempo
            estado = "OK" if ordenada else "FAIL"
            print(f"{estado} {nombre:25s} {tiempo*1000:8.4f} ms")
        except Exception as e:
            print(f"ERR {nombre:25s} Error: {e}")
            tiempos[nombre] = float("inf")
    print("=" * 70)
    tiempos_validos = {k: v for k, v in tiempos.items() if v != float("inf")}
    if tiempos_validos:
        mas_rapido = min(tiempos_validos, key=tiempos_validos.get)
        print(f"\nMétodo más rápido: {mas_rapido} ({tiempos_validos[mas_rapido]*1000:.4f} ms)")
    return tiempos


if __name__ == "__main__":
    print("=== Comparación de métodos ===\n")
    print("Lista pequeña (10 elementos):")
    lista_peq = generar_lista_aleatoria(10, 1, 50)
    print(f"Lista: {lista_peq}")
    comparar_metodos_ordenamiento(lista_peq)
    print("\nLista mediana (100 elementos):")
    lista_med = generar_lista_aleatoria(100, 1, 100)
    comparar_metodos_ordenamiento(lista_med)
