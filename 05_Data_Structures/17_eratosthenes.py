# -------------------------------------------------
# File Name: 17_eratosthenes.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Sieve of Eratosthenes. Finds all primes up to n by marking composites. O(n log log n).
# -------------------------------------------------

def sieve_of_eratosthenes(n):
    """Returns list of all primes up to n (inclusive)."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


def is_prime(n):
    """Returns True if n is prime. Checks divisors up to √n."""
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
    print("=== Mathematical Algorithms: Sieve of Eratosthenes ===\n")

    limit = 50
    primes = sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {primes}")
    print(f"Total: {len(primes)} primes")

    test_num = 97
    print(f"\nIs {test_num} prime? {is_prime(test_num)}")
