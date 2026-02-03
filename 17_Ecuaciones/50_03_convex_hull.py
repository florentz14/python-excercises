# Archivo: 50_03_convex_hull.py
# Descripción: Convex Hull (Graham Scan)

import math

print("=== 3. Convex Hull (Graham Scan) ===\n")


def orientacion(p, q, r):
    """Orientación del triple (p, q, r): 0 colineales, 1 horario, 2 antihorario."""
    valor = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if valor == 0:
        return 0
    return 1 if valor > 0 else 2


def graham_scan(puntos):
    """Convex Hull con Graham Scan. O(n log n)."""
    n = len(puntos)
    if n < 3:
        return puntos

    punto_inferior = min(puntos, key=lambda p: (p[1], p[0]))

    def angulo_polar(p):
        if p == punto_inferior:
            return (-1, 0, 0)
        dx = p[0] - punto_inferior[0]
        dy = p[1] - punto_inferior[1]
        return (0, -dy / math.sqrt(dx*dx + dy*dy), -(dx*dx + dy*dy))

    puntos_ordenados = sorted(puntos, key=angulo_polar)
    hull = [puntos_ordenados[0], puntos_ordenados[1]]

    for i in range(2, n):
        while len(hull) > 1 and orientacion(hull[-2], hull[-1], puntos_ordenados[i]) != 2:
            hull.pop()
        hull.append(puntos_ordenados[i])
    return hull


if __name__ == "__main__":
    puntos_hull = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    print(f"Puntos: {puntos_hull}")
    hull = graham_scan(puntos_hull)
    print(f"Convex Hull: {hull}")
