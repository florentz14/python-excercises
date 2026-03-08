# -------------------------------------------------
# File Name: 17_original.py
# Author: Florentino Báez
# Date: 17_Equations
# Description: Original numerical integration version.
# -------------------------------------------------

import scipy.integrate as spi


def integracion_original():
    """
    Versión original del código para calcular integrales.
    """
    def f(x):
        return (-x**2) - (2*x) + 8

    a = -4
    b = -3

    result, error = spi.quad(f, a, b)
    print(round(result, 2))


if __name__ == "__main__":
    print("=== Integración Numérica ===\n")
    print("Cálculo de integrales definidas usando métodos numéricos\n")
    print("=== Versión 1: Original ===\n")
    print("Resultado versión original:")
    integracion_original()
