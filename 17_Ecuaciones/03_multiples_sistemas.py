# Archivo: 25_03_multiples_sistemas.py
# Descripción: Resolver múltiples sistemas Ax = b simultáneamente

import numpy as np

from datos_sistema import A, B_multiple


def resolver_multiples_sistemas(A_mat, B):
    """
    Resuelve múltiples sistemas Ax = b para cada columna de B.

    Parámetros:
    - A_mat: Matriz de coeficientes
    - B: Matriz donde cada columna es un vector b diferente

    Retorna:
    - X: Matriz solución donde cada columna es una solución
    """
    try:
        X = np.linalg.solve(A_mat, B)
        return X
    except np.linalg.LinAlgError as e:
        print(f'Error: {e}')
        return None


if __name__ == "__main__":
    print("=== Versión 3: Múltiples Sistemas ===\n")
    print("Ejemplo: Resolver múltiples sistemas")
    print(f"Matriz B con múltiples sistemas:\n{B_multiple.T}")
    X_multiple = resolver_multiples_sistemas(A.copy(), B_multiple)
    if X_multiple is not None:
        print(f"\nSoluciones (cada columna es una solución):\n{X_multiple}")
