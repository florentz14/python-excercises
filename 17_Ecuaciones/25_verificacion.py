# Archivo: 31_09_verificacion.py
# Descripción: Verificación analítica vs numérica

import scipy.integrate as spi

from integracion_util import f_original


def verificar_integral_analitica(funcion, primitiva, a, b):
    """
    Compara el resultado numérico con el resultado analítico.
    """
    resultado_numerico, error = spi.quad(funcion, a, b)
    resultado_analitico = primitiva(b) - primitiva(a)
    diferencia = abs(resultado_numerico - resultado_analitico)

    print(f"\nVerificación para integral de {a} a {b}:")
    print(f"  Resultado numérico: {resultado_numerico:.8f}")
    print(f"  Resultado analítico: {resultado_analitico:.8f}")
    print(f"  Diferencia: {diferencia:.2e}")
    print(f"  Error numérico: {error:.2e}")

    if diferencia < 1e-6:
        print("  [OK] Coinciden (dentro de la tolerancia)")
    else:
        print("  [AVISO] Hay una diferencia significativa")

    return resultado_numerico, resultado_analitico


if __name__ == "__main__":
    print("=== Versión 9: Verificación Analítica vs Numérica ===\n")
    print("Verificación analítica para función original:")
    # Primitiva de f(x) = -x^2 - 2x + 8 es F(x) = -x^3/3 - x^2 + 8x
    primitiva_original = lambda x: (-x**3/3) - (x**2) + (8*x)
    verificar_integral_analitica(f_original, primitiva_original, -4, -3)
