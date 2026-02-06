# Archivo: 25_05_analisis_completo.py
# Descripción: Análisis completo del sistema de ecuaciones

import numpy as np

from datos_sistema import A, b


def analizar_sistema_completo(A_mat, b_vec):
    """
    Realiza un análisis completo del sistema de ecuaciones.
    """
    print("=" * 60)
    print("ANÁLISIS DEL SISTEMA DE ECUACIONES")
    print("=" * 60)

    print(f"\n1. Matriz de coeficientes A ({A_mat.shape[0]}x{A_mat.shape[1]}):")
    print(A_mat)

    print(f"\n2. Vector de términos independientes b:")
    print(b_vec)

    det = np.linalg.det(A_mat)
    print(f"\n3. Determinante: {det:.6f}")

    rango = np.linalg.matrix_rank(A_mat)
    print(f"4. Rango de la matriz: {rango}")

    cond = np.linalg.cond(A_mat)
    print(f"5. Número de condición: {cond:.2e}")
    if cond > 1e12:
        print("   [AVISO] Matriz mal condicionada (puede haber errores numéricos)")
    elif cond > 1e8:
        print("   [AVISO] Matriz moderadamente mal condicionada")
    else:
        print("   Matriz bien condicionada")

    if abs(det) > 1e-10:
        x = np.linalg.solve(A_mat, b_vec)
        print(f"\n6. Solución del sistema:")
        print(x)

        b_verif = np.dot(A_mat, x)
        error = np.linalg.norm(b_vec - b_verif)
        print(f"\n7. Verificación (A * x = b):")
        print(f"   Error: {error:.2e}")
        if error < 1e-10:
            print("   Solución verificada correctamente")
        else:
            print("   [AVISO] Error en la verificación")
    else:
        print("\n6. [AVISO] Sistema singular - no se puede resolver")

    print("=" * 60)


if __name__ == "__main__":
    print("=== Versión 5: Análisis Completo ===\n")
    analizar_sistema_completo(A.copy(), b.copy())
