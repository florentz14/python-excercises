# -------------------------------------------------
# File Name: 35_lineal.py
# Author: Florentino Báez
# Date: Data Structures - Search Algorithms
# Description: Linear Search.
#              Traverses the list sequentially comparing each
#              element with the target. Works with unsorted lists.
#              Includes optimized version for sorted lists and
#              search for all occurrences.
#              Complexity: O(n) in the worst case.
# -------------------------------------------------


def busqueda_lineal(lista, objetivo):
    """Searches element by element. Returns index or -1."""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  # Found → return position
    return -1  # Not found


def busqueda_lineal_optimizada(lista, objetivo):
    """If the list is sorted, stops when finding an element greater than target."""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
        if lista[indice] > objetivo:
            return -1  # In sorted list, it cannot be further ahead
    return -1


def busqueda_lineal_todas(lista, objetivo):
    """Returns list of all indices where the target appears."""
    indices = []
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            indices.append(indice)  # Store each position found
    return indices


if __name__ == "__main__":
    ejemplo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print("Lista:", ejemplo)
    print("Búsqueda lineal de 5:", busqueda_lineal(ejemplo, 5))
    print("Todas las ocurrencias de 5:", busqueda_lineal_todas(ejemplo, 5))
