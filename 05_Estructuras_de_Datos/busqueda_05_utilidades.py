"""
05_Estructuras_de_Datos - Funciones útiles para listas ordenadas
=================================================================
Posición de inserción (bisect_left), conteo de ocurrencias.
"""

from busqueda_01_binaria import (
    busqueda_binaria_primera_ocurrencia,
    busqueda_binaria_ultima_ocurrencia,
)


def encontrar_posicion_insercion(lista, objetivo):
    """Posición donde insertar para mantener orden (equivalente a bisect_left)."""
    izquierda, derecha = 0, len(lista)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio
    return izquierda


def contar_ocurrencias(lista_ordenada, objetivo):
    """Cuenta cuántas veces aparece objetivo en lista ordenada. O(log n)."""
    primera = busqueda_binaria_primera_ocurrencia(lista_ordenada, objetivo)
    if primera == -1:
        return 0
    ultima = busqueda_binaria_ultima_ocurrencia(lista_ordenada, objetivo)
    return ultima - primera + 1


if __name__ == "__main__":
    lista = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6]
    print("Lista:", lista)
    print("Posicion para insertar 3:", encontrar_posicion_insercion(lista, 3))
    print("Cantidad de 5s:", contar_ocurrencias(lista, 5))
