# -------------------------------------------------
# File Name: 57_tim_sort.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Tim Sort (Tim Peters, 2002).
#              Hybrid of Merge Sort + Insertion Sort. It is the
#              algorithm behind sorted() and list.sort() in
#              Python. Divides the list into "runs" of minimum size
#              (minrun), sorts them with Insertion Sort and merges
#              them. Excellent with partially sorted data.
#              O(n) best case, O(n log n) worst case.
# -------------------------------------------------

import random
import time


# ============================================================
# 1. Compute optimal minrun
# ============================================================
MIN_MERGE = 32


def calc_min_run(n):
    """
    Computes the minimum run size.
    Returns a value between 32 and 64 such that n/minrun is close
    to a power of 2 (for efficient merges).
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# ============================================================
# 2. Insertion Sort for small runs
# ============================================================
def insertion_sort_range(arr, left, right):
    """Insertion Sort in-place on range [left, right]."""
    for i in range(left + 1, right + 1):
        clave = arr[i]
        j = i - 1
        while j >= left and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave


# ============================================================
# 3. Merge of two adjacent runs
# ============================================================
def merge_runs(arr, left, mid, right):
    """
    Merges two sorted runs: arr[left..mid] and arr[mid+1..right].
    Optimized: only copies the smaller side to temporary buffer.
    """
    len_left = mid - left + 1
    len_right = right - mid

    # Copy to temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:  # <= for stability
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


# ============================================================
# 4. Tim Sort - Implementation
# ============================================================
def tim_sort(lista):
    """
    Tim Sort: hybrid of Merge Sort + Insertion Sort.
    Does not modify the original list.
    """
    arr = lista.copy()
    n = len(arr)

    if n <= 1:
        return arr

    min_run = calc_min_run(n)

    # Step 1: Create runs of size min_run using Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)

    # Step 2: Merge runs, doubling size each iteration
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge_runs(arr, left, mid, right)

        size *= 2

    return arr


# ============================================================
# 5. Demo: Tim Sort vs partially sorted data
# ============================================================
def demostrar_ventaja():
    """Shows the advantage of Tim Sort with partially sorted data."""
    n = 5000

    tipos_datos = {
        "Aleatorio":           [random.randint(1, 10000) for _ in range(n)],
        "Casi ordenado":       list(range(n)),  # Slightly shuffled below
        "Bloques ordenados":   [],              # Built below
        "Pocos únicos":        [random.choice(range(10)) for _ in range(n)],
        "Inversamente ord.":   list(range(n, 0, -1)),
    }

    # Almost sorted: swap 5% of elements
    casi = tipos_datos["Casi ordenado"]
    for _ in range(n // 20):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        casi[i], casi[j] = casi[j], casi[i]

    # Sorted blocks: 10 already sorted blocks, concatenated out of order
    bloques = []
    for _ in range(10):
        bloque = sorted([random.randint(1, 10000) for _ in range(n // 10)])
        bloques.extend(bloque)
    tipos_datos["Bloques ordenados"] = bloques

    print(f"\nRendimiento de Tim Sort vs sorted() ({n} elementos):")
    print("=" * 65)
    print(f"{'Tipo de datos':<22s} {'Tim Sort':>12s} {'sorted()':>12s}")
    print("-" * 65)

    for nombre, datos in tipos_datos.items():
        # Tim Sort
        copia1 = datos.copy()
        inicio = time.time()
        tim_sort(copia1)
        t_tim = time.time() - inicio

        # Python sorted()
        copia2 = datos.copy()
        inicio = time.time()
        sorted(copia2)
        t_python = time.time() - inicio

        print(f"  {nombre:<22s} {t_tim*1000:10.2f} ms {t_python*1000:10.2f} ms")


# ============================================================
# 6. Visual explanation of the process
# ============================================================
def tim_sort_visual(lista):
    """Shows the Tim Sort process step by step."""
    arr = lista.copy()
    n = len(arr)
    min_run = calc_min_run(n)

    print(f"\nTim Sort paso a paso")
    print(f"Lista original: {arr}")
    print(f"n = {n}, min_run = {min_run}")
    print(f"{'='*60}")

    # Step 1: Create runs
    print(f"\nPaso 1 - Crear runs (Insertion Sort en bloques de {min_run}):")
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        before = arr[start:end + 1].copy()
        insertion_sort_range(arr, start, end)
        after = arr[start:end + 1]
        print(f"  [{start}:{end+1}] {before} -> {after}")

    # Step 2: Merge
    print(f"\nPaso 2 - Merge de runs:")
    size = min_run
    paso = 0
    while size < n:
        paso += 1
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                print(f"  Merge [{left}:{mid+1}] + [{mid+1}:{right+1}]", end="")
                merge_runs(arr, left, mid, right)
                print(f" -> {arr[left:right+1]}")
        size *= 2

    print(f"\n{'='*60}")
    print(f"Resultado: {arr}")
    return arr


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Tim Sort ===\n")

    # Visual demo
    lista_demo = [5, 21, 7, 23, 19, 10, 42, 3, 15, 8, 31, 1, 27, 12]
    tim_sort_visual(lista_demo)

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
        resultado = tim_sort(caso)
        ok = all(resultado[i] <= resultado[i + 1]
                 for i in range(len(resultado) - 1)) if len(resultado) > 1 else True
        print(f"  {nombre:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {resultado[:8]}{'...' if len(resultado) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Advantage with partially sorted data
    demostrar_ventaja()

    print("\nNota: sorted() y list.sort() de Python usan Tim Sort internamente.")
    print("Esta implementación es educativa; la versión de CPython está en C.")
