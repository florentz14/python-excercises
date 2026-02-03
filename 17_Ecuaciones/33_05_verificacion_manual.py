# Archivo: 33_05_verificacion_manual.py
# Descripción: Verificación manual de la solución ecuación por ecuación

import numpy as np

from datos_ejemplo_33 import A, b


def verificar_solucion_manual(A_mat, b_vec, x):
    """
    Verifica la solución manualmente.
    """
    print("\nVerificación manual de la solución:")
    print("=" * 50)

    eq1 = x[0] + x[1] + x[2]
    print(f"Ecuación 1: x + y + z = {x[0]:.6f} + {x[1]:.6f} + {x[2]:.6f} = {eq1:.6f}")
    print(f"  Esperado: {b_vec[0]}, Diferencia: {abs(eq1 - b_vec[0]):.2e}")

    eq2 = 2*x[0] + x[2]
    print(f"\nEcuación 2: 2x + z = 2({x[0]:.6f}) + {x[2]:.6f} = {eq2:.6f}")
    print(f"  Esperado: {b_vec[1]}, Diferencia: {abs(eq2 - b_vec[1]):.2e}")

    eq3 = x[0] + 2*x[1]
    print(f"\nEcuación 3: x + 2y = {x[0]:.6f} + 2({x[1]:.6f}) = {eq3:.6f}")
    print(f"  Esperado: {b_vec[2]}, Diferencia: {abs(eq3 - b_vec[2]):.2e}")

    print("=" * 50)

    todas_correctas = (
        abs(eq1 - b_vec[0]) < 1e-10
        and abs(eq2 - b_vec[1]) < 1e-10
        and abs(eq3 - b_vec[2]) < 1e-10
    )
    print(f"\n[OK] Todas las ecuaciones se verifican: {todas_correctas}")


if __name__ == "__main__":
    print("=== Versión 5: Verificación Manual ===\n")
    x = np.linalg.solve(A, b)
    verificar_solucion_manual(A, b, x)
