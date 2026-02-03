# Archivo: 27_01_original.py
# Descripción: Versión original para resolver ecuaciones cuadráticas (solo reales)

import math


def ecuacion_cuadratica_original(a, b, c):
    """
    Versión original para resolver ecuaciones cuadráticas.
    Solo retorna soluciones reales.
    """
    condicional = b**2 - (4*a*c)
    if condicional > 0:
        x1 = (-b + math.sqrt(condicional))/(2*a)
        x2 = (-b - math.sqrt(condicional))/(2*a)
        return (x1, x2)
    elif condicional == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        return tuple()


if __name__ == "__main__":
    print("=== Ecuaciones Cuadráticas ===\n")
    print("Forma general: Ax^2 + Bx + C = 0, donde A != 0\n")
    print("=== Versión 1: Original ===\n")
    print("Pruebas del código original:")
    print(f"x² + 8x + 12 = 0: {ecuacion_cuadratica_original(1, 8, 12)}")
    print(f"x² + 2x + 1 = 0: {ecuacion_cuadratica_original(1, 2, 1)}")
    print(f"3x² - 8x + 6 = 0: {ecuacion_cuadratica_original(3, -8, 6)}")
