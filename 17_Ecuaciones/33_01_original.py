# Archivo: 33_01_original.py
# Descripción: Versión original del sistema de ecuaciones específico

import numpy as np


def resolver_sistema_original():
    """
    Versión original del código.
    """
    A = np.array([[1, 1, 1], [2, 0, 1], [1, 2, 0]])
    b = np.array([2, 1, 5])

    try:
        determinante = np.linalg.det(A)
        print(f'El determinante es: {round(determinante, 2)}')
        print()

        if determinante != 0:
            print('Solución del sistema:')
            x = np.linalg.solve(A, b)
            print(x)
            print()
            print('Comprobamos que A * x = b')
            print(np.matmul(A, x))
        else:
            print('La matriz es singular')
    except Exception as e:
        print(f'Ha ocurrido una excepción: {e}')


if __name__ == "__main__":
    print("=== Sistema de Ecuaciones Lineales (Ejemplo Específico) ===\n")
    print("=== Versión 1: Original ===\n")
    print("Ejecutando versión original:")
    resolver_sistema_original()
