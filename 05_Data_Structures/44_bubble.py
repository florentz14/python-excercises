# -------------------------------------------------
# File Name: 44_bubble.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Bubble Sort. Adjacent swaps, bubbles largest to end. O(n²). Stable. In-place.
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
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Bubble Sort:", bubble_sort(arr))
    print("Bubble Sort Optimized:", bubble_sort_optimizado(arr))
