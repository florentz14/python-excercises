"""
05_Estructuras_de_Datos - Insertion Sort (ordenamiento por inserción)
======================================================================
Complejidad: O(n²) peor, O(n) mejor. Estable. In-place. Bueno para listas pequeñas o casi ordenadas.
"""


def insertion_sort(lista):
    """Inserta cada elemento en su lugar dentro de la parte ya ordenada."""
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Insertion Sort:", insertion_sort(ejemplo))
