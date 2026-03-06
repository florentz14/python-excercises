# -------------------------------------------------
# File Name: 49_heap.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Heap Sort.
#              Builds a max-heap (largest always at the root)
#              and repeatedly extracts the maximum, placing it at
#              the end. Uses heapify to maintain the heap property
#              after each extraction.
#              Complexity: O(n log n). Not stable. In-place.
# -------------------------------------------------


def heap_sort(lista):
    """Builds max heap and repeatedly extracts the maximum."""
    lista = lista.copy()
    n = len(lista)
    # Step 1: Build max-heap (bottom-up from last parent node)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    # Step 2: Extract maximum and re-heapify
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]  # Move maximum to end
        heapify(lista, i, 0)  # Re-heapify the reduced heap
    return lista


def heapify(lista, n, i):
    """Adjusts the tree so that the root at i is a max-heap."""
    mayor = i                  # Assume current node is the largest
    izquierda = 2 * i + 1     # Left child
    derecha = 2 * i + 2       # Right child
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda      # Left child is larger
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha        # Right child is larger
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]  # Swap
        heapify(lista, n, mayor)  # Recursion: sink the displaced node


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Heap Sort:", heap_sort(ejemplo))
