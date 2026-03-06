# Archivo: 25_01_original.py
# Descripción: Versión original para resolver sistemas de ecuaciones lineales

import numpy as np

from datos_sistema import A, b


def resolver_sistema_original(A_mat, b_vec):
    """
    Versión original del código para resolver sistemas de ecuaciones lineales.
    """
    try:
        determinante = np.linalg.det(A_mat)
        print(f'El determinante es: {determinante}')
        print()

        if determinante != 0:
            print('Solución del sistema:')
            x = np.linalg.solve(A_mat, b_vec)
            print(x)
            print()
            print('Comprobamos que A * x = b')
            print(np.matmul(A_mat, x))
        else:
            print('La matriz es singular')
    except Exception as e:
        print(f'Ha ocurrido una excepción: {e}')


if __name__ == "__main__":
    print("=== Versión 1: Original ===\n")
    print("Sistema de ecuaciones:")
    print("Matriz A:")
    print(A)
    print("\nVector b (términos independientes):")
    print(b)
    print("\nResolviendo sistema...")
    resolver_sistema_original(A.copy(), b.copy())
