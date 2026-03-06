# Archivo: 31_05_comparar_metodos.py
# Descripción: Comparar métodos de integración numérica

import numpy as np
import scipy.integrate as spi

from integracion_util import f_original


def comparar_metodos_integracion(funcion, a, b):
    """
    Compara diferentes métodos de integración numérica.
    """
    print(f"\nComparando métodos de integración de {a} a {b}:")
    print("=" * 60)

    resultado_quad, error_quad = spi.quad(funcion, a, b)
    print(f"1. quad (adaptativo):")
    print(f"   Resultado: {resultado_quad:.8f}")
    print(f"   Error: {error_quad:.2e}")

    try:
        resultado_fixed, _ = spi.fixed_quad(funcion, a, b, n=50)
        print(f"\n2. fixed_quad (Gauss-Legendre, n=50):")
        print(f"   Resultado: {resultado_fixed:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_fixed):.2e}")
    except Exception as e:
        print(f"\n2. fixed_quad: Error - {e}")

    try:
        resultado_romberg = spi.romberg(funcion, a, b)
        print(f"\n3. romberg (extrapolación):")
        print(f"   Resultado: {resultado_romberg:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_romberg):.2e}")
    except Exception as e:
        print(f"\n3. romberg: Error - {e}")

    try:
        x = np.linspace(a, b, 1000)
        y = funcion(x)
        resultado_simpson = spi.simpson(y, x)
        print(f"\n4. simpson (regla de Simpson, 1000 puntos):")
        print(f"   Resultado: {resultado_simpson:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_simpson):.2e}")
    except Exception as e:
        print(f"\n4. simpson: Error - {e}")

    try:
        x = np.linspace(a, b, 1000)
        y = funcion(x)
        resultado_trapezoid = spi.trapezoid(y, x)
        print(f"\n5. trapezoid (regla del trapecio, 1000 puntos):")
        print(f"   Resultado: {resultado_trapezoid:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_trapezoid):.2e}")
    except Exception as e:
        print(f"\n5. trapezoid: Error - {e}")

    print("=" * 60)


if __name__ == "__main__":
    print("=== Versión 5: Comparación de Métodos ===\n")
    print("Comparando métodos para la función original:")
    comparar_metodos_integracion(f_original, -4, -3)
