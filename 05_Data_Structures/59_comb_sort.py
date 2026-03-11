# -------------------------------------------------
# File Name: 59_comb_sort.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Comb Sort. Improves bubble sort with larger gaps. O(n²) or better.
# -------------------------------------------------

import random
import time


# ============================================================
# 1. Basic Comb Sort
# ============================================================
def comb_sort(items):
    """
    Comb Sort: Bubble Sort with decreasing gaps.
    Shrink factor: 1.3 (optimal).
    Does not modify the original list.
    """
    items = items.copy()
    n = len(items)
    gap = n
    factor = 1.3  # Shrink factor
    swapped = True

    while gap > 1 or swapped:
        # Compute new gap
        gap = max(1, int(gap / factor))
        swapped = False

        # Compare and swap elements at distance 'gap'
        for i in range(n - gap):
            if items[i] > items[i + gap]:
                items[i], items[i + gap] = items[i + gap], items[i]
                swapped = True

    return items


# ============================================================
# 2. Comb Sort with "rule of 11"
# ============================================================
def comb_sort_11(items):
    """
    Comb Sort with the "Comb Sort 11" optimization:
    If gap is 9 or 10, force it to 11. This improves performance
    by avoiding certain patterns that cause poor performance.
    """
    items = items.copy()
    n = len(items)
    gap = n
    factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / factor))

        # Optimization: if gap is 9 or 10, use 11
        if gap == 9 or gap == 10:
            gap = 11

        swapped = False

        for i in range(n - gap):
            if items[i] > items[i + gap]:
                items[i], items[i + gap] = items[i + gap], items[i]
                swapped = True

    return items


# ============================================================
# 3. Comb Sort with visualization
# ============================================================
def comb_sort_visual(items):
    """Comb Sort with process visualization."""
    items = items.copy()
    n = len(items)
    gap = n
    factor = 1.3
    swapped = True
    step = 0

    print(f"\nOriginal list: {items}")
    print(f"{'='*60}")

    while gap > 1 or swapped:
        gap = max(1, int(gap / factor))
        swapped = False
        swaps = 0
        step += 1

        for i in range(n - gap):
            if items[i] > items[i + gap]:
                items[i], items[i + gap] = items[i + gap], items[i]
                swapped = True
                swaps += 1

        print(f"Step {step:2d} (gap={gap:2d}): {items}  ({swaps} swaps)")

    print(f"{'='*60}")
    print(f"Sorted list: {items}")
    return items


# ============================================================
# 4. Shrink factor comparison
# ============================================================
def comparar_factores(n=5000):
    """Compares different shrink factors."""
    items = [random.randint(1, 10000) for _ in range(n)]

    print(f"\nShrink factor comparison ({n} elements):")
    print("=" * 50)

    def comb_con_factor(items, factor):
        items = items.copy()
        n = len(items)
        gap = n
        swapped = True
        while gap > 1 or swapped:
            gap = max(1, int(gap / factor))
            swapped = False
            for i in range(n - gap):
                if items[i] > items[i + gap]:
                    items[i], items[i + gap] = items[i + gap], items[i]
                    swapped = True
        return items

    for factor in [1.1, 1.2, 1.3, 1.4, 1.5, 2.0]:
        copia = items.copy()
        start = time.time()
        result = comb_con_factor(copia, factor)
        tiempo = time.time() - start
        ok = all(result[i] <= result[i + 1]
                 for i in range(len(result) - 1))
        print(f"  Factor {factor:.1f}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nFactor 1.3 is generally the best choice.")


# ============================================================
# 5. Comparison with Bubble Sort and Shell Sort
# ============================================================
def bubble_sort(items):
    """Optimized Bubble Sort for comparison."""
    items = items.copy()
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def shell_sort(items):
    """Shell Sort for comparison."""
    items = items.copy()
    n = len(items)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = items[i]
            j = i
            while j >= gap and items[j - gap] > temp:
                items[j] = items[j - gap]
                j -= gap
            items[j] = temp
        gap //= 2
    return items


def compare_algorithms(n=3000):
    """Compares Comb Sort with Bubble Sort and Shell Sort."""
    items = [random.randint(1, 10000) for _ in range(n)]

    metodos = {
        "Bubble Sort":   bubble_sort,
        "Comb Sort":     comb_sort,
        "Comb Sort 11":  comb_sort_11,
        "Shell Sort":    shell_sort,
    }

    print(f"\nComparison ({n} random elements):")
    print("=" * 50)

    for name, metodo in metodos.items():
        copia = items.copy()
        start = time.time()
        result = metodo(copia)
        tiempo = time.time() - start
        ok = all(result[i] <= result[i + 1]
                 for i in range(len(result) - 1))
        print(f"  {name:15s}: {tiempo*1000:8.2f} ms {'OK' if ok else 'FAIL'}")

    print("\nComb Sort is usually much faster than Bubble Sort,")
    print("and often comparable to Shell Sort performance.")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Comb Sort ===\n")

    # Visual demo
    lista_demo = [8, 4, 1, 56, 3, 78, 45, 23, 12, 64]
    comb_sort_visual(lista_demo)

    # Functionality tests
    print("\n--- Tests ---")
    cases = {
        "Random":        [random.randint(1, 50) for _ in range(15)],
        "Already sorted": list(range(1, 11)),
        "Reverse":       list(range(10, 0, -1)),
        "All equal":     [5] * 8,
        "Single item":   [42],
        "Empty":         [],
    }

    for name, caso in cases.items():
        result = comb_sort(caso)
        ok = all(result[i] <= result[i + 1]
                 for i in range(len(result) - 1)) if len(result) > 1 else True
        print(f"  {name:15s}: {caso[:8]}{'...' if len(caso) > 8 else ''}"
              f" -> {result[:8]}{'...' if len(result) > 8 else ''}"
              f" {'OK' if ok else 'FAIL'}")

    # Comparisons
    comparar_factores(3000)
    compare_algorithms(2000)
