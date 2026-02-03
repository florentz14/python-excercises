# Archivo: 35_03_con_exacto.py
# Descripción: Sumas de Riemann comparadas con valor exacto

import scipy.integrate as spi

from riemann_util import f, a, b, n, suma_riemann_vectorizada


def suma_riemann_con_exacto(funcion, a_lim, b_lim, n_sub, mostrar_detalles=True):
    """
    Calcula sumas de Riemann y compara con el valor exacto.
    """
    left = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'izquierda')
    right = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'derecha')
    mid = suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, 'punto_medio')

    valor_exacto, error_exacto = spi.quad(funcion, a_lim, b_lim)
    error_left = abs(left - valor_exacto)
    error_right = abs(right - valor_exacto)
    error_mid = abs(mid - valor_exacto)

    if mostrar_detalles:
        print(f"\nIntegral de {a_lim} a {b_lim} con {n_sub} subintervalos:")
        print("=" * 60)
        print(f"Suma de Riemann izquierda:  {left:12.6f} (error: {error_left:.2e})")
        print(f"Suma de Riemann derecha:    {right:12.6f} (error: {error_right:.2e})")
        print(f"Suma de Riemann punto medio: {mid:12.6f} (error: {error_mid:.2e})")
        print(f"Valor exacto:                {valor_exacto:12.6f}")
        print("=" * 60)
        mejor = 'Punto medio' if error_mid < min(error_left, error_right) else ('Izquierda' if error_left < error_right else 'Derecha')
        print(f"\nMejor aproximación: {mejor}")

    return {
        'izquierda': left,
        'derecha': right,
        'punto_medio': mid,
        'exacto': valor_exacto,
        'errores': {'izquierda': error_left, 'derecha': error_right, 'punto_medio': error_mid}
    }


if __name__ == "__main__":
    print("=== Versión 3: Con Comparación con Valor Exacto ===\n")
    resultados = suma_riemann_con_exacto(f, a, b, n)
