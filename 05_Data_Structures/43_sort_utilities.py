# -------------------------------------------------
# File Name: 43_sort_utilities.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Sort utilities. Common helpers for sorting algorithms.
# -------------------------------------------------

import random


def esta_ordenada(lista):
    """Checks if a list is sorted in ascending order."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def generar_lista_aleatoria(n, minimo=1, maximo=100):
    """Generates a random list of n elements."""
    return [random.randint(minimo, maximo) for _ in range(n)]


if __name__ == "__main__":
    lista = generar_lista_aleatoria(5, 1, 20)
    print("Lista aleatoria:", lista)
    print("¿Ordenada?", esta_ordenada(lista))
    print("¿Ordenada [1,2,3]?", esta_ordenada([1, 2, 3]))
