# -------------------------------------------------
# File Name: 20_factorizacion.py
# Author: Florentino Báez
# Date: Estructuras de Datos - Algoritmos Matemáticos
# Description: Factorización en Primos y Conteo de Divisores.
#              Descompone un número en sus factores primos
#              dividiendo sucesivamente por el menor divisor
#              posible hasta √n. Incluye funciones para obtener
#              factores únicos y contar divisores totales.
#              Complejidad: O(√n).
# -------------------------------------------------

print("=== 6. Factorización de Números ===\n")


def factorizar(n):
    """
    Factoriza n en factores primos.
    Complejidad: O(√n)
    """
    factores = []
    divisor = 2  # Empezar con el primo más pequeño

    while divisor * divisor <= n:  # Solo probar hasta √n
        while n % divisor == 0:
            factores.append(divisor)  # Agregar el factor primo
            n //= divisor             # Dividir n por ese factor
        divisor += 1

    if n > 1:
        factores.append(n)  # Si queda n > 1, es un factor primo
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
