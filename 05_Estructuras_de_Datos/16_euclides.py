# -------------------------------------------------
# File Name: 16_euclides.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Euclid's Algorithm (GCD, LCM, Extended).
#              Computes the Greatest Common Divisor by repeatedly
#              dividing the larger by the smaller and taking
#              the remainder until 0. Includes extended version
#              that finds x, y such that a*x + b*y = GCD.
#              Complexity: O(log min(a, b)).
# -------------------------------------------------

print("=== 2. Algoritmo de Euclides (MCD) ===\n")


def euclides_mcd(a, b):
    """
    Greatest Common Divisor (Euclid's algorithm).
    Complexity: O(log min(a, b))
    """
    while b != 0:
        a, b = b, a % b  # Replace a with b, and b with the remainder
    return abs(a)


def euclides_mcd_recursivo(a, b):
    """Recursive version of Euclid's algorithm."""
    if b == 0:
        return abs(a)  # Base case: remainder is 0
    return euclides_mcd_recursivo(b, a % b)


def euclides_mcm(a, b):
    """Least Common Multiple: LCM(a, b) = |a * b| / GCD(a, b)."""
    mcd = euclides_mcd(a, b)
    return abs(a * b) // mcd if mcd != 0 else 0


def euclides_extendido(a, b):
    """
    Extended Euclid: finds x, y such that a*x + b*y = GCD(a, b).
    Returns: (gcd, x, y)
    """
    if a == 0:
        return abs(b), 0, 1 if b >= 0 else -1

    # Recursion: solve for (b % a, a) and reconstruct x, y
    mcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1  # Update coefficient x
    y = x1                    # Update coefficient y
    return mcd, x, y


if __name__ == "__main__":
    a_euclides = 48
    b_euclides = 18

    print(f"a = {a_euclides}, b = {b_euclides}")
    print(f"MCD (iterativo): {euclides_mcd(a_euclides, b_euclides)}")
    print(f"MCD (recursivo): {euclides_mcd_recursivo(a_euclides, b_euclides)}")
    print(f"MCM: {euclides_mcm(a_euclides, b_euclides)}")

    mcd_ext, x, y = euclides_extendido(a_euclides, b_euclides)
    print(f"Euclides extendido: {mcd_ext} = {a_euclides}*{x} + {b_euclides}*{y}")
