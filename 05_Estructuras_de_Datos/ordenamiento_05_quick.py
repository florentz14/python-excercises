"""
05_Estructuras_de_Datos - Quick Sort (ordenamiento rápido)
===========================================================
Complejidad: O(n log n) promedio, O(n²) peor. No estable. In-place posible.
"""


def quick_sort(lista):
    """Versión que usa listas auxiliares (clara). Pivote: elemento central."""
    if len(lista) <= 1:
        return lista.copy()
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


def quick_sort_inplace(lista, inicio=0, fin=None):
    """Quick sort in-place (modifica la lista)."""
    if fin is None:
        fin = len(lista) - 1
    if inicio < fin:
        pivote_idx = particionar(lista, inicio, fin)
        quick_sort_inplace(lista, inicio, pivote_idx - 1)
        quick_sort_inplace(lista, pivote_idx + 1, fin)
    return lista


def particionar(lista, inicio, fin):
    """Particiona alrededor del pivote (último elemento)."""
    pivote = lista[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Quick Sort:", quick_sort(ejemplo))
    copia = ejemplo.copy()
    quick_sort_inplace(copia)
    print("Quick Sort In-place:", copia)
