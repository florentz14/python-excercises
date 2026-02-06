# ---------------------------------------------------------------------------
# 34. Sieve of Eratosthenes - Primes up to n
# ---------------------------------------------------------------------------
# Descripción: Sieve of Eratosthenes - Primes up to n
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sieve(n: int) -> list[int]:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [i for i in range(2, n + 1) if is_prime[i]]


print(sieve(30))
