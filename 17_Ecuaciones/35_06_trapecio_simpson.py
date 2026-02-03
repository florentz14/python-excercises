# Archivo: 35_06_trapecio_simpson.py
# Descripción: Regla del trapecio y de Simpson

import scipy.integrate as spi

from riemann_util import f, a, b, n, suma_riemann_vectorizada, regla_trapecio, regla_simpson


if __name__ == "__main__":
    print("=== Versión 6: Regla del Trapecio y Simpson ===\n")
    print(f"Comparación de métodos para integral de {a} a {b} (n={n}):")
    valor_exacto, _ = spi.quad(f, a, b)

    left = suma_riemann_vectorizada(f, a, b, n, 'izquierda')
    right = suma_riemann_vectorizada(f, a, b, n, 'derecha')
    mid = suma_riemann_vectorizada(f, a, b, n, 'punto_medio')
    trapecio = regla_trapecio(f, a, b, n)
    simpson = regla_simpson(f, a, b, n)

    print("=" * 70)
    print(f"{'Método':<20} {'Aproximación':<20} {'Error':<20}")
    print("-" * 70)
    print(f"{'Riemann izquierda':<20} {left:<20.6f} {abs(left - valor_exacto):<20.2e}")
    print(f"{'Riemann derecha':<20} {right:<20.6f} {abs(right - valor_exacto):<20.2e}")
    print(f"{'Riemann punto medio':<20} {mid:<20.6f} {abs(mid - valor_exacto):<20.2e}")
    print(f"{'Regla del trapecio':<20} {trapecio:<20.6f} {abs(trapecio - valor_exacto):<20.2e}")
    print(f"{'Regla de Simpson':<20} {simpson:<20.6f} {abs(simpson - valor_exacto):<20.2e}")
    print("-" * 70)
    print(f"{'Valor exacto':<20} {valor_exacto:<20.6f} {'-':<20}")
    print("=" * 70)
