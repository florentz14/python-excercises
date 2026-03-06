# -------------------------------------------------
# File: 19_fibonacci_matematico.py (Fibonacci - Mathematical Methods)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Mathematical Algorithms
#
# Description:
#   Methods for computing the n-th Fibonacci number:
#   1) DP iterative: O(n) time, O(1) space - classic DP pattern.
#   2) Binet's formula: O(1) but loses precision for large n.
#   3) Matrix exponentiation [[1,1],[1,0]]^n: O(log n), exact.
# -------------------------------------------------

import math


def fibonacci_dp(n: int) -> int:
    """
    Dynamic Programming: iterative Fibonacci.
    Classic pattern with two variables. O(n) time, O(1) space.
    """
    # Handle small values directly
    if n <= 1:
        return n

    # Store the two previous Fibonacci values
    prev2, prev1 = 0, 1

    # Build up iteratively
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1

    return prev1


def fibonacci_binet(n):
    """
    n-th Fibonacci with Binet's formula.
    O(1) but with precision errors for large n.
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))


def fibonacci_matrix(n):
    """
    n-th Fibonacci via matrix exponentiation [[1,1],[1,0]]^n.
    Complexity: O(log n)
    """
    def mat_mult(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def mat_pow(M, k):
        if k == 1:
            return M
        half = mat_pow(M, k // 2)
        squared = mat_mult(half, half)
        return squared if k % 2 == 0 else mat_mult(M, squared)

    if n <= 1:
        return n

    base = [[1, 1], [1, 0]]
    M = mat_pow(base, n)
    return M[0][1]


if __name__ == "__main__":
    print("=== Mathematical Algorithms: Fibonacci ===\n")

    n = 10
    print(f"Fibonacci({n}):")
    print(f"  DP iterative: {fibonacci_dp(n)}")
    print(f"  Binet's formula: {fibonacci_binet(n)}")
    print(f"  Matrix exponentiation: {fibonacci_matrix(n)}")
