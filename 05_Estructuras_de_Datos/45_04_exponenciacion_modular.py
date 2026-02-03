# Archivo: 45_04_exponenciacion_modular.py
# Descripción: Exponenciación modular rápida

print("=== 4. Exponenciación Modular Rápida ===\n")


def exponenciacion_modular(base, exponente, modulo):
    """
    Calcula (base^exponente) mod modulo de forma eficiente.
    Complejidad: O(log exponente)
    """
    resultado = 1
    base = base % modulo

    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo

    return resultado


if __name__ == "__main__":
    base_exp = 3
    exp_exp = 100
    mod_exp = 7

    resultado = exponenciacion_modular(base_exp, exp_exp, mod_exp)
    print(f"({base_exp}^{exp_exp}) mod {mod_exp} = {resultado}")
    print(f"Verificación: {pow(base_exp, exp_exp, mod_exp)} (función built-in)")
