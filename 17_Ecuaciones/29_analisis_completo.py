# Archivo: 33_03_analisis_completo.py
# Descripción: Análisis completo del sistema de ecuaciones específico

import numpy as np
from fractions import Fraction

from datos_ejemplo_33 import A, b


def analizar_sistema_completo(A_mat, b_vec):
    """
    Analiza el sistema de ecuaciones completamente.
    """
    print("=" * 70)
    print("ANÁLISIS DEL SISTEMA DE ECUACIONES")
    print("=" * 70)

    print(f"\nSistema de ecuaciones:")
    print(f"  x + y + z = {b_vec[0]}")
    print(f"  2x + 0y + z = {b_vec[1]}")
    print(f"  x + 2y + 0z = {b_vec[2]}")

    print(f"\n1. Matriz de coeficientes A (3x3):")
    print(A_mat)

    print(f"\n2. Vector de términos independientes b:")
    print(b_vec)

    det = np.linalg.det(A_mat)
    print(f"\n3. Determinante:")
    print(f"   det(A) = {det:.6f}")
    print(f"   det(A) (redondeado) = {round(det, 2)}")

    rango = np.linalg.matrix_rank(A_mat)
    print(f"\n4. Rango de la matriz: {rango}")
    print(f"   Rango completo: {'Sí' if rango == A_mat.shape[0] else 'No'}")

    cond = np.linalg.cond(A_mat)
    print(f"\n5. Número de condición: {cond:.2e}")
    if cond > 1e12:
        print("   [AVISO] Matriz mal condicionada (puede haber errores numéricos)")
    elif cond > 1e8:
        print("   [AVISO] Matriz moderadamente mal condicionada")
    else:
        print("   Matriz bien condicionada")

    solucion = None
    if abs(det) > 1e-10:
        x = np.linalg.solve(A_mat, b_vec)
        solucion = x
        print(f"\n6. Solución del sistema:")
        print(f"   x = {x[0]:.6f} = {Fraction(x[0]).limit_denominator()}")
        print(f"   y = {x[1]:.6f} = {Fraction(x[1]).limit_denominator()}")
        print(f"   z = {x[2]:.6f} = {Fraction(x[2]).limit_denominator()}")
        print(f"   Vector solución: {x}")

        b_verif = np.dot(A_mat, x)
        error = np.linalg.norm(b_vec - b_verif)
        print(f"\n7. Verificación (A * x = b):")
        print(f"   A * x = {b_verif}")
        print(f"   b =     {b_vec}")
        print(f"   Error: {error:.2e}")
        if error < 1e-10:
            print("   Solución verificada correctamente")
        else:
            print("   [AVISO] Error en la verificación")

        print(f"\n8. Verificación ecuación por ecuación:")
        ecuaciones = [
            f"x + y + z = {x[0]:.6f} + {x[1]:.6f} + {x[2]:.6f} = {b_verif[0]:.6f} (esperado: {b_vec[0]})",
            f"2x + z = 2({x[0]:.6f}) + {x[2]:.6f} = {b_verif[1]:.6f} (esperado: {b_vec[1]})",
            f"x + 2y = {x[0]:.6f} + 2({x[1]:.6f}) = {b_verif[2]:.6f} (esperado: {b_vec[2]})"
        ]
        for eq in ecuaciones:
            print(f"   {eq}")
    else:
        print("\n6. [AVISO] Sistema singular - no se puede resolver")

    print("=" * 70)
    return solucion


if __name__ == "__main__":
    print("=== Versión 3: Análisis Completo ===\n")
    print("Análisis completo del sistema:")
    solucion = analizar_sistema_completo(A.copy(), b.copy())
