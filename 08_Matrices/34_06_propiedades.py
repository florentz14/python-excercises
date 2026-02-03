# Archivo: 34_06_propiedades.py
# Descripción: Propiedades del rango de matrices

import numpy as np

from rango_matriz_util import A


def propiedades_rango():
    """
    Demuestra propiedades importantes del rango de matrices.
    """
    print("\nPropiedades del Rango de Matrices:")
    print("=" * 70)

    A_t = A.T
    rango_A = np.linalg.matrix_rank(A)
    rango_At = np.linalg.matrix_rank(A_t)
    print(f"1. rank(A) = rank(A^T)")
    print(f"   rank(A) = {rango_A}")
    print(f"   rank(A^T) = {rango_At}")
    print(f"   Coinciden: {rango_A == rango_At}")

    if A.shape[1] >= 2:
        np.random.seed(42)
        B = np.random.rand(A.shape[1], 2)
        AB = A @ B
        rango_AB = np.linalg.matrix_rank(AB)
        rango_B = np.linalg.matrix_rank(B)
        print(f"\n2. rank(AB) <= min(rank(A), rank(B))")
        print(f"   rank(A) = {rango_A}, rank(B) = {rango_B}")
        print(f"   rank(AB) = {rango_AB}")
        print(f"   min(rank(A), rank(B)) = {min(rango_A, rango_B)}")
        print(f"   Se cumple: {rango_AB <= min(rango_A, rango_B)}")

    m, n = A.shape
    print(f"\n3. rank(A) <= min(m, n) para matriz {m}x{n}")
    print(f"   rank(A) = {rango_A}")
    print(f"   min({m}, {n}) = {min(m, n)}")
    print(f"   Se cumple: {rango_A <= min(m, n)}")

    print("=" * 70)


if __name__ == "__main__":
    print("=== Versión 6: Propiedades del Rango ===\n")
    propiedades_rango()
