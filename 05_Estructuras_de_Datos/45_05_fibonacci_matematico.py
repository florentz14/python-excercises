# Archivo: 45_05_fibonacci_matematico.py
# Descripción: Fibonacci con fórmula de Binet y exponenciación de matrices

import math

print("=== 5. Números de Fibonacci (Métodos Matemáticos) ===\n")


def fibonacci_binet(n):
    """
    n-ésimo Fibonacci con fórmula de Binet.
    O(1) pero con errores de precisión para n grandes.
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))


def fibonacci_matriz(n):
    """
    n-ésimo Fibonacci con exponenciación de matrices.
    Complejidad: O(log n)
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
