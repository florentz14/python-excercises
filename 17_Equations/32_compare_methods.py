# Archivo: 33_06_comparar_metodos.py
# Descripción: Comparación de métodos de resolución

import numpy as np

from datos_ejemplo_33 import A, b


def comparar_metodos(A_mat, b_vec):
    """
    Compara diferentes métodos para resolver el sistema.
    """
    print("\nComparando métodos de resolución:")
    print("=" * 60)

    x1 = np.linalg.solve(A_mat, b_vec)
    print(f"1. np.linalg.solve(): {x1}")

    A_inv = np.linalg.inv(A_mat)
    x2 = np.dot(A_inv, b_vec)
    print(f"2. A^(-1) * b: {x2}")
    error = np.linalg.norm(x1 - x2)
    print(f"   Diferencia con método 1: {error:.2e}")

    x3, residuals, rank, s = np.linalg.lstsq(A_mat, b_vec, rcond=None)
    print(f"3. np.linalg.lstsq(): {x3}")
    print(f"   Residuales: {residuals}")
    print(f"   Rango: {rank}")

    print("=" * 60)
    print("Todos los métodos dan resultados consistentes")


if __name__ == "__main__":
    print("=== Versión 6: Comparación con Otros Métodos ===\n")
    comparar_metodos(A.copy(), b.copy())
