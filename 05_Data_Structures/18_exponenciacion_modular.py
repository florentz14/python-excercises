# -------------------------------------------------
# File Name: 18_exponenciacion_modular.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Fast Modular Exponentiation.
#              Computes (base^exponent) mod modulo efficiently
#              using the repeated squaring method (binary exponentiation).
#              At each step, if the current bit of the exponent is 1,
#              multiply the result by the current base.
#              Complexity: O(log exponent).
# -------------------------------------------------

print("=== 4. Exponenciación Modular Rápida ===\n")


def exponenciacion_modular(base, exponente, modulo):
    """
    Computes (base^exponent) mod modulo efficiently.
    Complexity: O(log exponent)
    """
    resultado = 1
    base = base % modulo       # Reduce base to the modulo range

    while exponente > 0:
        if exponente % 2 == 1:
            # Current bit is 1: multiply result by current base
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1     # Shift bits right (divide by 2)
        base = (base * base) % modulo  # Square the base

    return resultado


if __name__ == "__main__":
    base_exp = 3
    exp_exp = 100
    mod_exp = 7

    resultado = exponenciacion_modular(base_exp, exp_exp, mod_exp)
    print(f"({base_exp}^{exp_exp}) mod {mod_exp} = {resultado}")
    print(f"Verificación: {pow(base_exp, exp_exp, mod_exp)} (función built-in)")
