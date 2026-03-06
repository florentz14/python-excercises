# Archivo: 31_03_multiples_funciones.py
# Descripción: Integrar múltiples funciones en el mismo intervalo

import numpy as np
import scipy.integrate as spi


def integrar_multiples_funciones(funciones_dict, a, b):
    """
    Integra múltiples funciones en el mismo intervalo.
    """
    print(f"\nIntegrando múltiples funciones de {a} a {b}:")
    print("=" * 60)

    resultados = {}
    for nombre, funcion in funciones_dict.items():
        resultado, error = spi.quad(funcion, a, b)
        resultados[nombre] = resultado
        print(f"{nombre:20s}: {resultado:10.6f} (error: {error:.2e})")

    print("=" * 60)
    return resultados


if __name__ == "__main__":
    print("=== Versión 3: Múltiples Funciones ===\n")

    funciones = {
        'Cuadrática original': lambda x: (-x**2) - (2*x) + 8,
        'x^2': lambda x: x**2,
        'sin(x)': lambda x: np.sin(x),
        'exp(x)': lambda x: np.exp(x),
        '1/x': lambda x: 1/x if x != 0 else 0
    }

    print("Integrando múltiples funciones de 1 a 2:")
    resultados = integrar_multiples_funciones(funciones, 1, 2)
