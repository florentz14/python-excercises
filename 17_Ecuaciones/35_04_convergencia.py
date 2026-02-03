# Archivo: 35_04_convergencia.py
# Descripción: Análisis de convergencia al variar n

import scipy.integrate as spi

from riemann_util import f, a, b, suma_riemann_vectorizada


def analizar_convergencia(funcion, a_lim, b_lim, n_valores=None):
    """
    Analiza cómo converge la aproximación con diferentes números de subintervalos.
    """
    if n_valores is None:
        n_valores = [10, 50, 100, 500, 1000, 5000]

    print(f"\nAnálisis de convergencia de {a_lim} a {b_lim}:")
    print("=" * 70)
    print(f"{'n':<8} {'Izquierda':<15} {'Derecha':<15} {'Punto Medio':<15} {'Error Punto Medio':<15}")
    print("-" * 70)

    valor_exacto, _ = spi.quad(funcion, a_lim, b_lim)

    for n_sub in n_valores:
        left = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'izquierda')
        right = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'derecha')
        mid = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'punto_medio')
        error_mid = abs(mid - valor_exacto)
        print(f"{n_sub:<8} {left:<15.6f} {right:<15.6f} {mid:<15.6f} {error_mid:<15.2e}")

    print("-" * 70)
    print(f"{'Exacto':<8} {'-':<15} {'-':<15} {valor_exacto:<15.6f} {'-':<15}")
    print("=" * 70)


if __name__ == "__main__":
    print("=== Versión 4: Análisis de Convergencia ===\n")
    analizar_convergencia(f, a, b)
