# Archivo: 50_05_interseccion_circulos.py
# Descripción: Intersección de dos círculos

import math

print("=== 5. Intersección de Círculos ===\n")


def interseccion_circulos(c1, r1, c2, r2):
    """
    Puntos de intersección entre dos círculos.
    c1, c2: centros (x, y); r1, r2: radios.
    Retorna lista de 0, 1 o 2 puntos.
    """
    x1, y1 = c1
    x2, y2 = c2
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if d > r1 + r2:
        return []
    if d < abs(r1 - r2):
        return []
    if d == 0 and r1 == r2:
        return []

    if d == r1 + r2 or d == abs(r1 - r2):
        t = r1 / d
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        return [(x, y)]

    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    x_m = x1 + a * (x2 - x1) / d
    y_m = y1 + a * (y2 - y1) / d
    x3 = x_m + h * (y2 - y1) / d
    y3 = y_m - h * (x2 - x1) / d
    x4 = x_m - h * (y2 - y1) / d
    y4 = y_m + h * (x2 - x1) / d
    return [(x3, y3), (x4, y4)]


if __name__ == "__main__":
    circulo1 = (0, 0)
    radio1 = 5
    circulo2 = (8, 0)
    radio2 = 3
    intersecciones = interseccion_circulos(circulo1, radio1, circulo2, radio2)
    print(f"Círculo 1: centro {circulo1}, radio {radio1}")
    print(f"Círculo 2: centro {circulo2}, radio {radio2}")
    print(f"Puntos de intersección: {intersecciones}")
    for i, punto in enumerate(intersecciones, 1):
        print(f"  Punto {i}: ({punto[0]:.4f}, {punto[1]:.4f})")
