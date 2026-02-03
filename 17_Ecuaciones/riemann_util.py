# Archivo: riemann_util.py
# Descripción: Utilidades para sumas de Riemann

import numpy as np
import scipy.integrate as spi

# Parámetros del ejemplo: intervalo [a, b] y número de subintervalos
a = -1.38
b = 2.88
n = 1000


def f(x):
    """Función a integrar: -x^2 + (3x/2) + 4"""
    return (-x**2) + ((3*x)/2) + 4


def suma_riemann_vectorizada(funcion, a_lim, b_lim, n_sub, metodo='punto_medio'):
    """
    Calcula suma de Riemann usando NumPy vectorizado.

    Parámetros:
    - funcion: Función a integrar
    - a_lim, b_lim: Límites de integración
    - n_sub: Número de subintervalos
    - metodo: 'izquierda', 'derecha', 'punto_medio'

    Retorna:
    - Aproximación de la integral
    """
    dx = (b_lim - a_lim) / n_sub

    if metodo == 'izquierda':
        x = np.linspace(a_lim, b_lim - dx, n_sub)
    elif metodo == 'derecha':
        x = np.linspace(a_lim + dx, b_lim, n_sub)
    elif metodo == 'punto_medio':
        x = np.linspace(a_lim + dx/2, b_lim - dx/2, n_sub)
    else:
        raise ValueError("Método debe ser 'izquierda', 'derecha' o 'punto_medio'")

    valores = funcion(x)
    return np.sum(valores) * dx


def regla_trapecio(funcion, a_lim, b_lim, n_sub):
    """Aproximación usando la regla del trapecio."""
    dx = (b_lim - a_lim) / n_sub
    x = np.linspace(a_lim, b_lim, n_sub + 1)
    y = funcion(x)
    suma = (y[0] + y[-1]) / 2 + np.sum(y[1:-1])
    return suma * dx


def regla_simpson(funcion, a_lim, b_lim, n_sub):
    """Aproximación usando la regla de Simpson. n debe ser par."""
    if n_sub % 2 != 0:
        n_sub += 1
    dx = (b_lim - a_lim) / n_sub
    x = np.linspace(a_lim, b_lim, n_sub + 1)
    y = funcion(x)
    suma = y[0] + y[-1]
    suma += 4 * np.sum(y[1:-1:2])
    suma += 2 * np.sum(y[2:-1:2])
    return (dx / 3) * suma
