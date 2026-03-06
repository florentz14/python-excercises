# -------------------------------------------------
# File Name: 19_fibonacci_matematico.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Fibonacci with Mathematical Methods.
#              Computes the n-th Fibonacci using two approaches:
#              1) Binet's formula (phi^n): O(1) but loses
#              precision for large n.
#              2) Matrix exponentiation [[1,1],[1,0]]^n: O(log n)
#              exact using matrix multiplication.
# -------------------------------------------------

import math

print("=== 5. Números de Fibonacci (Métodos Matemáticos) ===\n")


def fibonacci_binet(n):
    """
    n-th Fibonacci with Binet's formula.
    O(1) but with precision errors for large n.
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))


def fibonacci_matriz(n):
    """
    n-th Fibonacci with matrix exponentiation.
    Complexity: O(log n)
    """
    def multiplicar_matrices(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def potencia_matriz_fib(M, k):
        if k == 1:
            return M
        if k % 2 == 0:
            mitad = potencia_matriz_fib(M, k // 2)
            return multiplicar_matrices(mitad, mitad)
        return multiplicar_matrices(M, potencia_matriz_fib(M, k - 1))

    if n <= 1:
        return n

    matriz_base = [[1, 1], [1, 0]]
    matriz_potencia = potencia_matriz_fib(matriz_base, n)
    return matriz_potencia[0][1]


if __name__ == "__main__":
    n_fib_mate = 10
    print(f"Fibonacci({n_fib_mate}):")
    print(f"  Fórmula de Binet: {fibonacci_binet(n_fib_mate)}")
    print(f"  Matriz: {fibonacci_matriz(n_fib_mate)}")
