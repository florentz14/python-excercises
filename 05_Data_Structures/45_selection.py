# -------------------------------------------------
# File Name: 45_selection.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Selection Sort.
#              In each iteration finds the minimum element of the
#              unsorted subarray and swaps it with the first
#              element of that subarray. Always does O(n²)
#              comparisons regardless of the case.
#              Complexity: O(n²). Not stable. In-place.
# -------------------------------------------------


def selection_sort(lista):
    """At each step places the minimum of the rest at the current position."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i  # Assume the minimum is at the current position
        # Find the minimum in the unsorted subarray
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j  # Update minimum index
        # Swap the minimum with the current position
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Selection Sort:", selection_sort(ejemplo))
