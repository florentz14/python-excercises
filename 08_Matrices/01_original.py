# Archivo: 34_01_original.py
# Descripción: Versión original para calcular el rango de una matriz

import numpy as np


def rango_matriz_original():
    """
    Versión original del código para calcular el rango de una matriz.
    """
    A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])
    print(A)
    resultado = np.linalg.matrix_rank(A)
    print(resultado)


if __name__ == "__main__":
    print("=== Rango de una Matriz ===\n")
    print("El rango de una matriz es el número de filas (o columnas) linealmente independientes.\n")
    print("=== Versión 1: Original ===\n")
    print("Resultado versión original:")
    rango_matriz_original()
