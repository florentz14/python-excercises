"""
05_Estructuras_de_Datos - Utilidades para métodos de ordenamiento
==================================================================
"""

import random


def esta_ordenada(lista):
    """Verifica si una lista está ordenada de forma ascendente."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def generar_lista_aleatoria(n, minimo=1, maximo=100):
    """Genera una lista aleatoria de n elementos."""
    return [random.randint(minimo, maximo) for _ in range(n)]


if __name__ == "__main__":
    lista = generar_lista_aleatoria(5, 1, 20)
    print("Lista aleatoria:", lista)
    print("¿Ordenada?", esta_ordenada(lista))
    print("¿Ordenada [1,2,3]?", esta_ordenada([1, 2, 3]))
