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
        # Gap insertion sort: compare elements gap positions apart
        for i in range(gap, n):
            temp = lista[i]
            j = i
            # Shift elements gap positions right while current is smaller
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
    step = 0

    print(f"\nOriginal: {lista}")
    print(f"{'='*60}")

    while gap > 0:
        step += 1
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp

        print(f"Step {step} (gap={gap}): {lista}")
        gap //= 2

    print(f"{'='*60}")
    print(f"Sorted: {lista}")
    return lista


# ============================================================
# 5. Gap sequence comparison
# ============================================================
def compare_gap_sequences(n=5000):
    """Compares performance of different gap sequences (Shell, Knuth, Hibbard)."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    secuencias = {
        "Shell (n/2)":  shell_sort,
        "Knuth":        shell_sort_knuth,
        "Hibbard":      shell_sort_hibbard,
    }

    print(f"\nGap sequence comparison ({n} elements):")
    print("=" * 50)

    for name, method in secuencias.items():
        copy_arr = lista.copy()
        start_t = time.time()
        result = method(copy_arr)
        elapsed = time.time() - start_t
        is_ok = all(result[i] <= result[i + 1] for i in range(len(result) - 1))
        status = "OK" if is_ok else "FAIL"
        print(f"  {status} {name:15s}: {elapsed*1000:8.2f} ms")


# ============================================================
# 6. Shell Sort vs Insertion Sort comparison
# ============================================================
def insertion_sort(arr):
    """Insertion Sort for comparison with Shell Sort."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def compare_with_insertion(n=3000):
    """Compares Shell Sort vs Insertion Sort on random data."""
    lista = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Insertion Sort": insertion_sort,
        "Shell Sort":     shell_sort,
        "Shell (Knuth)":  shell_sort_knuth,
    }

    print(f"\nShell Sort vs Insertion Sort ({n} elements):")
    print("=" * 50)

    for name, method in metodos.items():
        copy_arr = lista.copy()
        start_t = time.time()
        method(copy_arr)
        elapsed = time.time() - start_t
        print(f"  {name:20s}: {elapsed*1000:8.2f} ms")

    print("\nShell Sort is much faster than Insertion Sort on random data")
    print("because it moves distant elements before refining locally.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Shell Sort ===\n")

    # Visual demo with small list
    lista_demo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    shell_sort_visual(lista_demo)

    # Functionality tests
    print("\n--- Tests ---")
    cases = {
        "Random":    [random.randint(1, 50) for _ in range(15)],
        "Sorted":    list(range(1, 11)),
        "Reverse":   list(range(10, 0, -1)),
        "All same":  [5] * 8,
        "Single":    [42],
        "Empty":     [],
    }

    for name, case in cases.items():
        result = shell_sort(case)
        ok = all(result[i] <= result[i + 1] for i in range(len(result) - 1)) if len(result) > 1 else True
        print(f"  {name:15s}: {str(case[:8])}{'...' if len(case) > 8 else ''} -> {str(result[:8])}{'...' if len(result) > 8 else ''} {'OK' if ok else 'FAIL'}")

    # Comparisons
    compare_gap_sequences(3000)
    compare_with_insertion(3000)
