# -------------------------------------------------
# File Name: 46_insertion.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Insertion Sort.
#              Takes each element and inserts it into its correct
#              position within the already sorted portion, shifting
#              larger elements to the right. Excellent for small
#              or nearly sorted lists (O(n) best case).
#              Complexity: O(n²) worst case. Stable. In-place.
# -------------------------------------------------


def insertion_sort(lista):
    """Inserts each element into its place within the already sorted portion."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]  # Element to insert
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave  # Insert key at its correct position
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Insertion Sort:", insertion_sort(ejemplo))
