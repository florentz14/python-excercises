"""
05_Estructuras_de_Datos - Búsqueda binaria (Binary Search)
===========================================================
Complejidad: O(log n). Requiere lista ordenada.
"""


def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria iterativa. Devuelve índice o -1."""
    if not lista:
        return -1
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    """Búsqueda binaria recursiva."""
    if derecha is None:
        derecha = len(lista) - 1
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    if lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


def busqueda_binaria_primera_ocurrencia(lista, objetivo):
    """Índice de la primera ocurrencia (lista con duplicados)."""
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
    """Índice de la última ocurrencia (lista con duplicados)."""
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
