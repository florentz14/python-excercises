# Archivo: resolver_cuadratica.py
# Descripción: Resolver ecuaciones cuadráticas Ax² + Bx + C = 0 (versión completa)

import math
import cmath


def ecuacion_cuadratica_completa(a, b, c, solo_reales=False):
    """
    Resuelve ecuaciones cuadráticas, incluyendo soluciones complejas.

    Parámetros:
    - a, b, c: Coeficientes de la ecuación Ax² + Bx + C = 0
    - solo_reales: Si True, retorna solo soluciones reales (tuple vacío si son complejas)

    Retorna:
    - Tupla con las soluciones (puede ser 0, 1 o 2 soluciones)
    """
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero (no es una ecuación cuadrática)")

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        return (x1, x2)
    elif discriminante == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        if solo_reales:
            return tuple()
        raiz = cmath.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        return (x1, x2)
