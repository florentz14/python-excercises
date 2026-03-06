# Archivo: 35_02_optimizada.py
# Descripción: Sumas de Riemann vectorizadas con NumPy

from riemann_util import f, a, b, n, suma_riemann_vectorizada


if __name__ == "__main__":
    print("=== Versión 2: Optimizada (Vectorizada) ===\n")
    print(f"Sumas de Riemann (vectorizadas) para f(x) de {a} a {b} con {n} subintervalos:")
    left = suma_riemann_vectorizada(f, a, b, n, 'izquierda')
    right = suma_riemann_vectorizada(f, a, b, n, 'derecha')
    mid = suma_riemann_vectorizada(f, a, b, n, 'punto_medio')
    print(f"  Suma izquierda: {left:.6f}")
    print(f"  Suma derecha: {right:.6f}")
    print(f"  Suma punto medio: {mid:.6f}")
