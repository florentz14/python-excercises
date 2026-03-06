# Archivo: 33_04_paso_a_paso.py
# Descripción: Solución paso a paso (matriz aumentada)

import numpy as np

from datos_ejemplo_33 import A, b


def resolver_paso_a_paso(A_mat, b_vec):
    """
    Muestra el proceso de resolución paso a paso.
    """
    print("\nResolución paso a paso usando eliminación gaussiana:")
    print("(Nota: numpy usa métodos optimizados internamente)")
    print()

    A_aumentada = np.column_stack([A_mat, b_vec])
    print("Matriz aumentada [A|b]:")
    print(A_aumentada)
    print()

    x = np.linalg.solve(A_mat, b_vec)
    print("Solución encontrada:")
    print(f"  x = {x[0]:.6f}")
    print(f"  y = {x[1]:.6f}")
    print(f"  z = {x[2]:.6f}")

    return x


if __name__ == "__main__":
    print("=== Versión 4: Solución Paso a Paso (Método de Eliminación) ===\n")
    resolver_paso_a_paso(A.copy(), b.copy())
