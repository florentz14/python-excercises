# -------------------------------------------------
# File Name: 55_shell_sort.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Shell Sort (1959).
#              Generalization of Insertion Sort that allows
#              swapping distant elements using decreasing
#              gaps. When gap is 1, it becomes Insertion Sort
#              on nearly sorted data. Includes Shell, Knuth
#              and Hibbard sequences.
#              Complexity: O(n^(3/2)) with Knuth. In-place.
# -------------------------------------------------

import time
import random


# ============================================================
# 1. Shell Sort - Shell sequence (n/2)
# ============================================================
def shell_sort(lista):
    """
    Shell Sort with Shell gap sequence: n/2, n/4, ..., 1
    Does not modify the original list.
    """
    lista = lista.copy()
    n = len(lista)
    gap = n // 2  # Initial gap

    while gap > 0:
        # Insertion Sort with current gap
        for i in range(gap, n):
            temp = lista[i]
            j = i
            # Move elements that are 'gap' distance apart
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  # Reduce gap

    return lista


# ============================================================
# 2. Shell Sort - Knuth sequence
# ============================================================
def shell_sort_knuth(lista):
    """
    Shell Sort with Knuth gap sequence: 1, 4, 13, 40, 121, ...
    Formula: gap = (3^k - 1) / 2
    Better performance than Shell sequence.
    """
    lista = lista.copy()
    n = len(lista)

    # Compute initial Knuth gap (largest that is < n/3)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1  # 1, 4, 13, 40, 121, 364, ...

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 3  # Reduce using inverse Knuth sequence

    return lista


# ============================================================
# 3. Shell Sort - Hibbard sequence
# ============================================================
def shell_sort_hibbard(lista):
    """
    Shell Sort with Hibbard gap sequence: 1, 3, 7, 15, 31, ...
    Formula: 2^k - 1
    Worst case complexity: O(n^(3/2))
    """
    lista = lista.copy()
    n = len(lista)

    # Generate Hibbard sequence
    gaps = []
    k = 1
    while (2**k - 1) < n:
        gaps.append(2**k - 1)
        k += 1

    # Traverse gaps from largest to smallest
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

    return lista


# ============================================================
# 4. Step-by-step visualization
# ============================================================
def shell_sort_visual(lista):
    """Shell Sort with visualization of each gap step."""
    lista = lista.copy()
    n = len(lista)
    gap = n // 2
    paso = 0

    print(f"\nLista original: {lista}")
    print(f"{'='*60}")

    while gap > 0:
        paso += 1
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

        print(f"Paso {paso} (gap={gap}): {lista}")
        gap //= 2

    print(f"{'='*60}")
    print(f"Lista ordenada: {lista}")
    return lista


# ============================================================
# 5. Gap sequence comparison
# ============================================================
def comparar_secuencias(n=5000):
    """Compares performance of different gap sequences."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    secuencias = {
        "Shell (n/2)":  shell_sort,
        "Knuth":        shell_sort_knuth,
        "Hibbard":      shell_sort_hibbard,
    }

    print(f"\nComparación de secuencias de gaps ({n} elementos):")
    print("=" * 50)

    for nombre, metodo in secuencias.items():
        copia = lista.copy()
        inicio = time.time()
        resultado = metodo(copia)
        tiempo = time.time() - inicio
        ordenada = all(resultado[i] <= resultado[i + 1]
                       for i in range(len(resultado) - 1))
        estado = "OK" if ordenada else "FAIL"
        print(f"  {estado} {nombre:15s}: {tiempo*1000:8.2f} ms")


# ============================================================
# 6. Shell Sort vs Insertion Sort comparison
# ============================================================
def insertion_sort(lista):
    """Insertion Sort for comparison."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def comparar_con_insertion(n=3000):
    """Compares Shell Sort vs Insertion Sort."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Insertion Sort": insertion_sort,
        "Shell Sort":     shell_sort,
        "Shell (Knuth)":  shell_sort_knuth,
    }

    print(f"\nShell Sort vs Insertion Sort ({n} elementos):")
    print("=" * 50)

    for nombre, metodo in metodos.items():
        copia = lista.copy()
        inicio = time.time()
        metodo(copia)
        tiempo = time.time() - inicio
        print(f"  {nombre:20s}: {tiempo*1000:8.2f} ms")

    print("\nShell Sort es mucho más rápido que Insertion Sort")
    print("porque mueve elementos lejanos antes de refinar.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Shell Sort ===\n")

    # Visual demo with small list
    lista_demo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    shell_sort_visual(lista_demo)

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
        resultado = shell_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparisons
    comparar_secuencias(3000)
    comparar_con_insertion(3000)
