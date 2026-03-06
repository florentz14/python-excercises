# Archivo: 31_01_original.py
# Descripción: Versión original de integración numérica

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
