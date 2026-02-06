"""
05_Estructuras_de_Datos - Bubble Sort (ordenamiento de burbuja)
================================================================
Complejidad: O(n²). Estable. In-place.
"""


def bubble_sort(lista):
    """Bubble sort clásico. No modifica la lista original."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_optimizado(lista):
    """Se detiene si no hay intercambios (lista ya ordenada)."""
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista


if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Bubble Sort:", bubble_sort(ejemplo))
    print("Bubble Sort Optimizado:", bubble_sort_optimizado(ejemplo))
