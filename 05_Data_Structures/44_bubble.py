# -------------------------------------------------
# File Name: 44_bubble.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Bubble Sort.
#              Compares pairs of adjacent elements and
#              swaps them if they are out of order, "bubbling"
#              the largest to the end in each pass. Optimized
#              version stops if no swaps occur in a pass.
#              Complexity: O(n²). Stable. In-place.
# -------------------------------------------------


def bubble_sort(lista):
    """Classic bubble sort. Does not modify the original list."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        # In each pass, the largest element "bubbles" to the end
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Swap out-of-order adjacent elements
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_optimizado(lista):
    """Stops if no swaps occur (list already sorted)."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        intercambiado = False  # Flag to detect if any changes occurred
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break  # List already sorted → terminate early
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Bubble Sort:", bubble_sort(ejemplo))
    print("Bubble Sort Optimizado:", bubble_sort_optimizado(ejemplo))
