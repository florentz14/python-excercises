# Archivo: 35_01_original.py
# Descripción: Versión original de sumas de Riemann

import numpy as np


def suma_riemann_original():
    """
    Versión original del código para calcular sumas de Riemann.
    """
    def f(x):
        return (-x**2) + ((3*x)/2) + 4

    a = -1.38
    b = 2.88
    n = 1000
    dx = (b - a) / n

    left_sum = 0
    for i in range(n):
        left_sum += f(a + i*dx)

    upper_sum = 0
    for i in range(1, n+1):
        upper_sum += f(a + i*dx)

    mid_sum = 0
    for i in range(n):
        mid_sum += f(a + (i+0.5)*dx)

    left_sum *= dx
    upper_sum *= dx
    mid_sum *= dx

    print("Suma de Riemann izquierda:", left_sum)
    print("Suma de Riemann superior:", upper_sum)
    print("Suma de Riemann punto medio:", mid_sum)


if __name__ == "__main__":
    print("=== Sumas de Riemann ===\n")
    print("Aproximación numérica de integrales usando sumas de Riemann\n")
    print("=== Versión 1: Original ===\n")
    print("Ejecutando versión original:")
    suma_riemann_original()
