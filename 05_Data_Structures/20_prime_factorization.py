# -------------------------------------------------
# File: 20_factorizacion.py (Prime Factorization & Divisor Count)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Mathematical Algorithms
#
# Description:
#   Prime factorization by trial division: divide n by the smallest
#   prime divisor until n=1. Also: unique prime factors and total
#   divisor count (using exponents in factorization).
#
# Complexity: O(√n).
# -------------------------------------------------


def factorize(n):
    """Returns list of prime factors (with duplicates)."""
    factors = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)
    return factors


def unique_prime_factors(n):
    """Returns set of unique prime factors."""
    return list(set(factorize(n)))


def count_divisors(n):
    """Returns number of positive divisors of n."""
    factors = factorize(n)
    count = {}
    for f in factors:
        count[f] = count.get(f, 0) + 1
    result = 1
    for exp in count.values():
        result *= (exp + 1)
    return result


if __name__ == "__main__":
    print("=== Mathematical Algorithms: Prime Factorization ===\n")

    num = 60
    factors = factorize(num)
    unique = unique_prime_factors(num)
    div_count = count_divisors(num)

    print(f"Number: {num}")
    print(f"Prime factors: {factors}")
    print(f"Unique factors: {unique}")
    print(f"Number of divisors: {div_count}")
