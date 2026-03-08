# -------------------------------------------------
# File Name: 58_vector_modulus.py
# Description: Compute vector modulus (magnitude)
# -------------------------------------------------

import math


def vector_modulus(v: list[float]) -> float:
    """Return |v| = sqrt(sum of squares)."""
    return math.sqrt(sum(x * x for x in v))


if __name__ == "__main__":
    print(vector_modulus([3, 4]))
    print(vector_modulus([1, 1, 1]))
    print(vector_modulus([1.0, 0.0, 0.0]))
