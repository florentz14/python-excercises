# Archivo: 25_04_fracciones.py
# Descripción: Resolver sistema y mostrar solución en fracciones

import numpy as np
from fractions import Fraction

from datos_sistema import A, b


def resolver_sistema_fracciones(A_mat, b_vec):
    """
    Resuelve el sistema y muestra la solución en fracciones.
    """
    try:
        x = np.linalg.solve(A_mat, b_vec)

        print("Solución en decimales:")
        print(x)

        print("\nSolución en fracciones:")
        for i, valor in enumerate(x):
            frac = Fraction(valor).limit_denominator()
            print(f"  x[{i}] = {frac} = {float(frac):.6f}")

        return x
    except Exception as e:
        print(f'Error: {e}')
        return None


if __name__ == "__main__":
    print("=== Versión 4: Mostrar Solución en Fracciones ===\n")
    print("Resolviendo y mostrando en fracciones:")
    resolver_sistema_fracciones(A.copy(), b.copy())
