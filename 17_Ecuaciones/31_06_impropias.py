# Archivo: 31_06_impropias.py
# Descripción: Integrales impropias (límites infinitos o discontinuidades)

import numpy as np
import scipy.integrate as spi


def integrar_impropia(funcion, a, b, tipo='infinito'):
    """
    Calcula integrales impropias (límites infinitos o discontinuidades).
    """
    print(f"\nIntegral impropia ({tipo}):")

    try:
        if tipo == 'infinito':
            resultado, error = spi.quad(funcion, a, np.inf)
            print(f"  Integral f(x)dx de {a} a inf = {resultado:.6f} (error: {error:.2e})")
        elif tipo == 'discontinuidad':
            resultado, error = spi.quad(funcion, a, b, points=[0])
            print(f"  Integral f(x)dx de {a} a {b} = {resultado:.6f} (error: {error:.2e})")
        else:
            resultado, error = spi.quad(funcion, a, b)
            print(f"  Resultado: {resultado:.6f} (error: {error:.2e})")

        return resultado, error
    except Exception as e:
        print(f"  Error: {e}")
        return None, None


if __name__ == "__main__":
    print("=== Versión 6: Integrales Impropias ===\n")
    print("Ejemplo: Integral impropia")
    funcion_impropia = lambda x: np.exp(-x)
    resultado_impropia, error_impropia = integrar_impropia(
        funcion_impropia, 0, np.inf, tipo='infinito'
    )
