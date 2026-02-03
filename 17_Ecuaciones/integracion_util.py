# Archivo: integracion_util.py
# Descripción: Funciones compartidas para integración numérica

import scipy.integrate as spi


def f_original(x):
    """Función del ejemplo original: f(x) = -x^2 - 2x + 8"""
    return (-x**2) - (2*x) + 8


def integrar_funcion(funcion, a, b, mostrar_detalles=True):
    """
    Calcula la integral definida de una función entre a y b.

    Parámetros:
    - funcion: Función a integrar
    - a: Límite inferior
    - b: Límite superior
    - mostrar_detalles: Si mostrar información detallada

    Retorna:
    - resultado: Valor de la integral
    - error: Estimación del error
    """
    resultado, error = spi.quad(funcion, a, b)

    if mostrar_detalles:
        print(f"Integral de {a} a {b}:")
        print(f"  Resultado: {resultado:.6f}")
        print(f"  Error estimado: {error:.2e}")
        print(f"  Resultado redondeado (2 decimales): {round(resultado, 2)}")

    return resultado, error
