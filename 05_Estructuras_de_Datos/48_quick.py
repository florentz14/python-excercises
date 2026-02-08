# -------------------------------------------------
# File Name: 48_quick.py
# Author: Florentino Báez
# Date: Data Structures - Sorting Algorithms
# Description: Quick Sort.
#              Chooses a pivot and partitions the list into smaller,
#              equal, and larger. Recursively sorts the partitions.
#              Includes clear version with auxiliary lists and
#              in-place version with Lomuto partition.
#              Complexity: O(n log n) average, O(n²) worst case.
# -------------------------------------------------


def quick_sort(lista):
    """Version that uses auxiliary lists (clear). Pivot: middle element."""
    if len(lista) <= 1:
        return lista.copy()
    pivote = lista[len(lista) // 2]                   # Choose middle pivot
    menores = [x for x in lista if x < pivote]        # Smaller elements
    iguales = [x for x in lista if x == pivote]       # Equal elements
    mayores = [x for x in lista if x > pivote]        # Larger elements
    return quick_sort(menores) + iguales + quick_sort(mayores)


def quick_sort_inplace(lista, inicio=0, fin=None):
    """Quick sort in-place (modifies the list)."""
    if fin is None:
        fin = len(lista) - 1
    if inicio < fin:
        pivote_idx = particionar(lista, inicio, fin)           # Partition
        quick_sort_inplace(lista, inicio, pivote_idx - 1)      # Sort left
        quick_sort_inplace(lista, pivote_idx + 1, fin)         # Sort right
    return lista


def particionar(lista, inicio, fin):
    """Partitions around the pivot (last element) - Lomuto scheme."""
    pivote = lista[fin]           # Pivot = last element
    i = inicio - 1                # Index of last smaller element
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]  # Move smaller to the left
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]  # Place pivot in position
    return i + 1  # Final pivot position


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Quick Sort:", quick_sort(ejemplo))
    copia = ejemplo.copy()
    quick_sort_inplace(copia)
    print("Quick Sort In-place:", copia)
