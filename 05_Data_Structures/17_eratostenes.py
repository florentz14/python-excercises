# -------------------------------------------------
# File Name: 17_eratostenes.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Sieve of Eratosthenes and Prime Verification.
#              The sieve marks multiples of each found prime as
#              composite, starting from i² (smaller ones were
#              already marked). Also includes optimized individual
#              verification by testing divisors only up to √n.
#              Sieve complexity: O(n log log n). Verification: O(√n).
# -------------------------------------------------

print("=== 3. Criba de Eratóstenes ===\n")


def criba_eratostenes(n):
    """
    Finds all prime numbers up to n.
    Complexity: O(n log log n)
    """
    if n < 2:
        return []

    es_primo = [True] * (n + 1)  # Assume all primes initially
    es_primo[0] = es_primo[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):  # Only up to √n
        if es_primo[i]:
            # Mark all multiples of i as not prime (from i²)
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    # Collect numbers still marked as prime
    return [i for i in range(2, n + 1) if es_primo[i]]


def es_primo_optimizado(n):
    """
    Checks whether n is prime.
    Complexity: O(√n)
    """
    if n < 2:
        return False
    if n == 2:
        return True       # 2 is the only even prime
    if n % 2 == 0:
        return False       # Discard evens > 2
    # Test only odd divisors up to √n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False   # Found a divisor → not prime
    return True


if __name__ == "__main__":
    limite_criba = 50
    primos = criba_eratostenes(limite_criba)
    print(f"Números primos hasta {limite_criba}: {primos}")
    print(f"Total: {len(primos)} primos")

    numero_test = 97
    print(f"\n¿{numero_test} es primo? {es_primo_optimizado(numero_test)}")
