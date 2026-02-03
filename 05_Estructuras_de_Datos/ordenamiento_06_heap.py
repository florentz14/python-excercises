"""
05_Estructuras_de_Datos - Heap Sort (ordenamiento por montículos)
==================================================================
Complejidad: O(n log n). No estable. In-place.
"""


def heap_sort(lista):
    """Construye heap máximo y extrae el máximo repetidamente."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista


def heapify(lista, n, i):
    """Ajusta el árbol para que la raíz en i sea un heap máximo."""
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Heap Sort:", heap_sort(ejemplo))
