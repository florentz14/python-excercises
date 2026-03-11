# -------------------------------------------------
# File Name: 16_euclid.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Euclidean algorithm for GCD. Computes greatest common divisor efficiently. O(log min(a,b)).
# -------------------------------------------------

def gcd(a, b):
    """Greatest Common Divisor (iterative)."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a, b):
    """GCD recursive version."""
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def lcm(a, b):
    """Least Common Multiple: LCM(a,b) = |a*b| / GCD(a,b)."""
    g = gcd(a, b)
    return abs(a * b) // g if g != 0 else 0


def extended_gcd(a, b):
    """Returns (gcd, x, y) such that a*x + b*y = gcd(a,b)."""
    if a == 0:
        return abs(b), 0, 1 if b >= 0 else -1

    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


if __name__ == "__main__":
    print("=== Mathematical Algorithms: Euclid's GCD ===\n")

    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (iterative): {gcd(a, b)}")
    print(f"GCD (recursive): {gcd_recursive(a, b)}")
    print(f"LCM: {lcm(a, b)}")

    g, x, y = extended_gcd(a, b)
    print(f"Extended: {g} = {a}*{x} + {b}*{y}")
