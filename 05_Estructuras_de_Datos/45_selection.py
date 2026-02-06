"""
05_Estructuras_de_Datos - Selection Sort (ordenamiento por selección)
======================================================================
Complejidad: O(n²). No estable. In-place.
"""


def selection_sort(lista):
    """En cada paso coloca el mínimo del resto en la posición actual."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Selection Sort:", selection_sort(ejemplo))
