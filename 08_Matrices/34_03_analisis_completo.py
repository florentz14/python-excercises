# Archivo: 34_03_analisis_completo.py
# Descripción: Análisis completo del rango de la matriz

import numpy as np

from rango_matriz_util import A


def analizar_rango_completo(A_mat):
    """
    Realiza un análisis completo del rango de la matriz.
    """
    print("=" * 70)
    print("ANÁLISIS DEL RANGO DE LA MATRIZ")
    print("=" * 70)

    print(f"\nMatriz A ({A_mat.shape[0]}x{A_mat.shape[1]}):")
    print(A_mat)

    rango = np.linalg.matrix_rank(A_mat)
    print(f"\n1. Rango de la matriz: {rango}")

    rango_maximo = min(A_mat.shape)
    print(f"2. Rango máximo posible: min({A_mat.shape[0]}, {A_mat.shape[1]}) = {rango_maximo}")

    print(f"\n3. Tipo de matriz:")
    if rango == rango_maximo:
        print("   Matriz de rango completo (full rank)")
        print("   -> Todas las filas (o columnas) son linealmente independientes")
    else:
        print("   [AVISO] Matriz de rango reducido (rank deficient)")
        dependencias = rango_maximo - rango
        print(f"   -> {dependencias} fila(s) o columna(s) son linealmente dependientes")

    if A_mat.shape[0] == A_mat.shape[1]:
        det = np.linalg.det(A_mat)
        print(f"\n4. Determinante (matriz cuadrada): {det:.6f}")
        if abs(det) < 1e-10:
            print("   [AVISO] Determinante ~ 0 -> Matriz singular")
            print(f"   -> El rango es menor que {A_mat.shape[0]}")
        else:
            print("   Determinante != 0 -> Matriz no singular")
            print(f"   -> El rango es {A_mat.shape[0]} (rango completo)")

    print(f"\n5. Espacios fundamentales:")
    print(f"   Dimensión del espacio de columnas: {rango}")
    print(f"   Dimensión del espacio de filas: {rango}")
    if A_mat.shape[0] == A_mat.shape[1]:
        print(f"   Dimensión del espacio nulo: {A_mat.shape[0] - rango}")

    print("=" * 70)
    return rango


if __name__ == "__main__":
    print("=== Versión 3: Análisis Completo ===\n")
    print("Análisis completo:")
    rango_completo = analizar_rango_completo(A.copy())
