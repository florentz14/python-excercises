# Archivo: 35_07_completo.py
# Descripción: Función completa con todas las aproximaciones de Riemann

import scipy.integrate as spi

from riemann_util import f, a, b, n, suma_riemann_vectorizada, regla_trapecio, regla_simpson


def integrar_riemann_completo(funcion, a_lim, b_lim, n_sub=1000, mostrar_detalles=True):
    """
    Función completa que calcula todas las aproximaciones de Riemann.
    """
    resultados = {}

    resultados['izquierda'] = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'izquierda')
    resultados['derecha'] = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'derecha')
    resultados['punto_medio'] = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'punto_medio')
    resultados['trapecio'] = regla_trapecio(funcion, a_lim, b_lim, n_sub)
    resultados['simpson'] = regla_simpson(funcion, a_lim, b_lim, n_sub)
    resultados['exacto'], _ = spi.quad(funcion, a_lim, b_lim)

    if mostrar_detalles:
        print(f"Integral aproximada de {a_lim} a {b_lim} (n={n_sub} subintervalos):")
        print("=" * 70)
        for metodo, valor in resultados.items():
            if metodo != 'exacto':
                error = abs(valor - resultados['exacto'])
                print(f"{metodo.capitalize():<15} {valor:12.6f} (error: {error:.2e})")
        print("-" * 70)
        print(f"{'Exacto':<15} {resultados['exacto']:12.6f}")
        print("=" * 70)

    return resultados


if __name__ == "__main__":
    print("=== Versión 7: Función Completa Mejorada ===\n")
    print("Análisis completo:")
    resultados_completos = integrar_riemann_completo(f, a, b, n_sub=1000)
