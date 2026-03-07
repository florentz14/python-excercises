# Archivo: 25_07_comparar_metodos.py
# Descripción: Comparar métodos para resolver el sistema

import numpy as np

from datos_sistema import A, b


def comparar_metodos(A_mat, b_vec):
    """
    Compara diferentes métodos para resolver el sistema.
    """
    print(f"\nComparando métodos para el sistema Ax = b")
    print(f"Matriz A:\n{A_mat}")
    print(f"Vector b: {b_vec}\n")

    try:
        x1 = np.linalg.solve(A_mat, b_vec)
        print(f"1. np.linalg.solve(): {x1}")
    except Exception as e:
        print(f"1. np.linalg.solve(): Error - {e}")
        x1 = None

    try:
        A_inv = np.linalg.inv(A_mat)
        x2 = np.dot(A_inv, b_vec)
        print(f"2. A^(-1) * b: {x2}")
        if x1 is not None:
            error = np.linalg.norm(x1 - x2)
            print(f"   Diferencia con método 1: {error:.2e}")
    except Exception as e:
        print(f"2. A^(-1) * b: Error - {e}")

    try:
        x3, residuals, rank, s = np.linalg.lstsq(A_mat, b_vec, rcond=None)
        print(f"3. np.linalg.lstsq(): {x3}")
        print(f"   Residuales: {residuals}")
    except Exception as e:
        print(f"3. np.linalg.lstsq(): Error - {e}")


if __name__ == "__main__":
    print("=== Versión 7: Ejemplos y Comparación ===\n")
    comparar_metodos(A.copy(), b.copy())
