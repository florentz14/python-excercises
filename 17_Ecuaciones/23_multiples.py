# Archivo: 31_07_multiples.py
# Descripción: Integrales dobles (y triples)

import scipy.integrate as spi


def integrar_doble(funcion, a, b, c, d):
    """
    Calcula integrales dobles.
    ∫∫ f(x,y) dx dy
    """
    try:
        resultado, error = spi.dblquad(funcion, a, b, lambda x: c, lambda x: d)
        print(f"\nIntegral doble:")
        print(f"  ∫∫ f(x,y) dx dy")
        print(f"  x: [{a}, {b}], y: [{c}, {d}]")
        print(f"  Resultado: {resultado:.6f}")
        print(f"  Error: {error:.2e}")
        return resultado, error
    except Exception as e:
        print(f"  Error: {e}")
        return None, None


if __name__ == "__main__":
    print("=== Versión 7: Integrales Múltiples ===\n")
    print("Ejemplo: Integral doble")
    # dblquad espera funcion(y, x) para ∫∫ f dx dy con x en [a,b], y en [c,d]
    funcion_doble = lambda y, x: x * y
    resultado_doble, error_doble = integrar_doble(funcion_doble, 0, 1, 0, 1)
