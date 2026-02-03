"""
05_Estructuras_de_Datos - Búsqueda lineal (Linear Search)
==========================================================
Complejidad: O(n). Funciona con listas no ordenadas.
"""


def busqueda_lineal(lista, objetivo):
    """Busca elemento por elemento. Devuelve índice o -1."""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1


def busqueda_lineal_optimizada(lista, objetivo):
    """Si la lista está ordenada, para al encontrar un elemento mayor."""
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
        if lista[indice] > objetivo:
            return -1
    return -1


def busqueda_lineal_todas(lista, objetivo):
    """Devuelve lista de todos los índices donde aparece el objetivo."""
    indices = []
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            indices.append(indice)
    return indices


if __name__ == "__main__":
    ejemplo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print("Lista:", ejemplo)
    print("Búsqueda lineal de 5:", busqueda_lineal(ejemplo, 5))
    print("Todas las ocurrencias de 5:", busqueda_lineal_todas(ejemplo, 5))
