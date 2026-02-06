# Archivo: rango_matriz_util.py
# Descripción: Utilidades compartidas para el cálculo del rango de matrices

import numpy as np

# Matriz del ejemplo original (3x4)
A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])


def calcular_rango_matriz(A_mat, mostrar_info=True):
    """
    Calcula el rango de una matriz con información adicional.

    Parámetros:
    - A_mat: Matriz numpy
    - mostrar_info: Si mostrar información detallada

    Retorna:
    - rango: Rango de la matriz
    - info: Diccionario con información adicional
    """
    rango = np.linalg.matrix_rank(A_mat)

    if mostrar_info:
        print(f"Matriz ({A_mat.shape[0]}x{A_mat.shape[1]}):")
        print(A_mat)
        print(f"\nRango de la matriz: {rango}")
        print(f"Rango máximo posible: min({A_mat.shape[0]}, {A_mat.shape[1]}) = {min(A_mat.shape)}")

        if rango == min(A_mat.shape):
            print("Matriz de rango completo (full rank)")
        else:
            print("Matriz de rango reducido (rank deficient)")
            print(f"   Dependencias: {min(A_mat.shape) - rango} fila(s) o columna(s) dependientes")

    info = {
        'rango': rango,
        'forma': A_mat.shape,
        'rango_maximo': min(A_mat.shape),
        'rango_completo': rango == min(A_mat.shape)
    }

    return rango, info
