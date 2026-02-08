# -------------------------------------------------
# File Name: 36_binaria.py
# Author: Florentino Báez
# Date: Data Structures - Search Algorithms
# Description: Binary Search.
#              Divides the sorted list in half at each step,
#              discarding the half where the target cannot be.
#              Includes iterative, recursive, first and
#              last occurrence versions for lists with duplicates.
#              Complexity: O(log n). Requires sorted list.
# -------------------------------------------------


def busqueda_binaria(lista, objetivo):
    """Iterative binary search. Returns index or -1."""
    if not lista:
        return -1
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Midpoint of range
        if lista[medio] == objetivo:
            return medio                     # Found
        if lista[medio] < objetivo:
            izquierda = medio + 1            # Search right half
        else:
            derecha = medio - 1              # Search left half
    return -1  # Not found


def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    """Recursive binary search."""
    if derecha is None:
        derecha = len(lista) - 1
    if izquierda > derecha:
        return -1  # Base case: empty range
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    if lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


def busqueda_binaria_primera_ocurrencia(lista, objetivo):
    """Index of the first occurrence (list with duplicates)."""
    izquierda, derecha = 0, len(lista) - 1
    resultado = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            resultado = medio
            derecha = medio - 1
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return resultado


def busqueda_binaria_ultima_ocurrencia(lista, objetivo):
    """Index of the last occurrence (list with duplicates)."""
    izquierda, derecha = 0, len(lista) - 1
    resultado = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            resultado = medio
            izquierda = medio + 1
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return resultado


if __name__ == "__main__":
    lista_ord = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print("Lista ordenada:", lista_ord)
    print("Búsqueda binaria de 5:", busqueda_binaria(lista_ord, 5))
    print("Primera ocurrencia de 5:", busqueda_binaria_primera_ocurrencia(lista_ord, 5))
    print("Última ocurrencia de 5:", busqueda_binaria_ultima_ocurrencia(lista_ord, 5))
