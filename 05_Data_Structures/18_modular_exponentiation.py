# -------------------------------------------------
# File Name: 18_modular_exponentiation.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Fast modular exponentiation. (base^exp) mod m via repeated squaring. Binary exponentiation. O(log exponent).
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
