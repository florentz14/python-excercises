# -------------------------------------------------
# File Name: 59_comb_sort.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Comb Sort.
#              Improvement of Bubble Sort that compares elements at
#              distance 'gap' which is reduced by factor 1.3 in each
#              pass. When gap = 1, it is Bubble Sort. Eliminates
#              "turtles" like Shell Sort does with Insertion Sort.
#              Includes "Comb Sort 11" variant and comparison of
#              shrink factors.
#              Complexity: O(n log n) best, O(n²) worst case.
# -------------------------------------------------

import random
import time


# ============================================================
# 1. Basic Comb Sort
# ============================================================
def comb_sort(lista):
    """
    Comb Sort: Bubble Sort with decreasing gaps.
    Shrink factor: 1.3 (optimal).
    Does not modify the original list.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3  # Shrink factor
    intercambiado = True

    while gap > 1 or intercambiado:
        # Compute new gap
        gap = max(1, int(gap / factor))
        intercambiado = False

        # Compare and swap elements at distance 'gap'
        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True

    return lista


# ============================================================
# 2. Comb Sort with "rule of 11"
# ============================================================
def comb_sort_11(lista):
    """
    Comb Sort with the "Comb Sort 11" optimization:
    If gap is 9 or 10, force it to 11. This improves performance
    by avoiding certain patterns that cause poor performance.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3
    intercambiado = True

    while gap > 1 or intercambiado:
        gap = max(1, int(gap / factor))

        # Optimization: if gap is 9 or 10, use 11
        if gap == 9 or gap == 10:
            gap = 11

        intercambiado = False

        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True

    return lista


# ============================================================
# 3. Comb Sort with visualization
# ============================================================
def comb_sort_visual(lista):
    """Comb Sort with process visualization."""
    lista = lista.copy()
    n = len(lista)
    gap = n
    factor = 1.3
    intercambiado = True
    paso = 0

    print(f"\nLista original: {lista}")
    print(f"{'='*60}")

    while gap > 1 or intercambiado:
        gap = max(1, int(gap / factor))
        intercambiado = False
        swaps = 0
        paso += 1

        for i in range(n - gap):
            if lista[i] > lista[i + gap]:
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                intercambiado = True
                swaps += 1

        print(f"Paso {paso:2d} (gap={gap:2d}): {lista}  ({swaps} swaps)")

    print(f"{'='*60}")
    print(f"Lista ordenada: {lista}")
    return lista


# ============================================================
# 4. Shrink factor comparison
# ============================================================
def comparar_factores(n=5000):
    """Compares different shrink factors."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    print(f"\nComparación de factores de reducción ({n} elementos):")
    print("=" * 50)

    def comb_con_factor(lista, factor):
        lista = lista.copy()
        n = len(lista)
        gap = n
        intercambiado = True
        while gap > 1 or intercambiado:
            gap = max(1, int(gap / factor))
            intercambiado = False
            for i in range(n - gap):
                if lista[i] > lista[i + gap]:
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    intercambiado = True
        return lista

    for factor in [1.1, 1.2, 1.3, 1.4, 1.5, 2.0]:
        copia = lista.copy()
        inicio = time.time()
        resultado = comb_con_factor(copia, factor)
        tiempo = time.time() - inicio
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1))
        print(f"  Factor {factor:.1f}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nEl factor 1.3 es generalmente el mejor.")


# ============================================================
# 5. Comparison with Bubble Sort and Shell Sort
# ============================================================
def bubble_sort(lista):
    """Optimized Bubble Sort for comparison."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista


def shell_sort(lista):
    """Shell Sort for comparison."""
    lista = lista.copy()
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista


def comparar(n=3000):
    """Compares Comb Sort with Bubble Sort and Shell Sort."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Bubble Sort":   bubble_sort,
        "Comb Sort":     comb_sort,
        "Comb Sort 11":  comb_sort_11,
        "Shell Sort":    shell_sort,
    }

    print(f"\nComparación ({n} elementos aleatorios):")
    print("=" * 50)

    for nombre, metodo in metodos.items():
        copia = lista.copy()
        inicio = time.time()
        resultado = metodo(copia)
        tiempo = time.time() - inicio
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1))
        print(f"  {nombre:15s}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nComb Sort es mucho más rápido que Bubble Sort,")
    print("y comparable a Shell Sort en rendimiento.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Comb Sort ===\n")

    # Visual demo
    lista_demo = [8, 4, 1, 56, 3, 78, 45, 23, 12, 64]
    comb_sort_visual(lista_demo)

    # Functionality tests
    print("\n--- Pruebas ---")
    casos = {
        "Aleatoria":     [random.randint(1, 50) for _ in range(15)],
        "Ya ordenada":   list(range(1, 11)),
        "Inversa":       list(range(10, 0, -1)),
        "Iguales":       [5] * 8,
        "Un elemento":   [42],
        "Vacía":         [],
    }

    for nombre, caso in casos.items():
        resultado = comb_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparisons
    comparar_factores(3000)
    comparar(2000)
