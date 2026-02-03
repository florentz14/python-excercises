# Archivo: 45_03_eratostenes.py
# Descripción: Criba de Eratóstenes y verificación de primos

print("=== 3. Criba de Eratóstenes ===\n")


def criba_eratostenes(n):
    """
    Encuentra todos los números primos hasta n.
    Complejidad: O(n log log n)
    """
    if n < 2:
        return []

    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    return [i for i in range(2, n + 1) if es_primo[i]]


def es_primo_optimizado(n):
    """
    Verifica si n es primo.
    Complejidad: O(√n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    limite_criba = 50
    primos = criba_eratostenes(limite_criba)
    print(f"Números primos hasta {limite_criba}: {primos}")
    print(f"Total: {len(primos)} primos")

    numero_test = 97
    print(f"\n¿{numero_test} es primo? {es_primo_optimizado(numero_test)}")
