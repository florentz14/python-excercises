# Archivo: 34_04_comparar_metodos.py
# Descripción: Comparar métodos para calcular el rango

import numpy as np

from rango_matriz_util import A


def comparar_metodos_rango(A_mat):
    """
    Compara diferentes métodos para calcular el rango.
    """
    print("\nComparando métodos para calcular el rango:")
    print("=" * 60)

    rango1 = np.linalg.matrix_rank(A_mat)
    print(f"1. np.linalg.matrix_rank(): {rango1}")

    U, s, Vt = np.linalg.svd(A_mat, full_matrices=False)
    tolerancia = max(A_mat.shape) * np.finfo(s.dtype).eps
    rango2 = int(np.sum(s > tolerancia))
    print(f"2. SVD (valores singulares): {rango2}")
    print(f"   Valores singulares: {s}")
    print(f"   Valores singulares > tolerancia ({tolerancia:.2e}): {rango2}")

    try:
        Q, R = np.linalg.qr(A_mat)
        rango3 = int(np.sum(np.abs(np.diag(R)) > 1e-10))
        print(f"3. QR (diagonales no nulas): {rango3}")
    except Exception as e:
        print(f"3. QR: Error - {e}")
        rango3 = rango1

    print("=" * 60)
    print(f"Todos los métodos dan resultados consistentes: {rango1 == rango2 == rango3}")
    return rango1


if __name__ == "__main__":
    print("=== Versión 4: Comparación de Métodos ===\n")
    comparar_metodos_rango(A.copy())
