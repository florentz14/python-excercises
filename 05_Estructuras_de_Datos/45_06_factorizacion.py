# Archivo: 45_06_factorizacion.py
# Descripción: Factorización en primos y conteo de divisores

print("=== 6. Factorización de Números ===\n")


def factorizar(n):
    """
    Factoriza n en factores primos.
    Complejidad: O(√n)
    """
    factores = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factores.append(n)
    return factores


def factores_unicos(n):
    """Factores primos únicos de n."""
    return list(set(factorizar(n)))


def contar_divisores(n):
    """Número de divisores de n."""
    factores = factorizar(n)
    conteo = {}
    for factor in factores:
        conteo[factor] = conteo.get(factor, 0) + 1
    divisores = 1
    for exponente in conteo.values():
        divisores *= (exponente + 1)
    return divisores


if __name__ == "__main__":
    numero_factorizar = 60
    factores = factorizar(numero_factorizar)
    factores_uni = factores_unicos(numero_factorizar)
    divisores = contar_divisores(numero_factorizar)

    print(f"Número: {numero_factorizar}")
    print(f"Factores primos: {factores}")
    print(f"Factores únicos: {factores_uni}")
    print(f"Número de divisores: {divisores}")
