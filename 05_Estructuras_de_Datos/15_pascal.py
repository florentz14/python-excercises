# -------------------------------------------------
# File Name: 15_pascal.py
# Author: Florentino Báez
# Date: Data Structures - Mathematical Algorithms
# Description: Pascal's Triangle and Binomial Coefficients.
#              Generates rows of the triangle where each element is
#              the sum of the two above it. Allows computing
#              binomial coefficients C(n, k) and generating
#              individual rows efficiently.
#              Complexity: O(n²) for n full rows.
# -------------------------------------------------

print("=== Algoritmos Matemáticos ===\n")
print("=== 1. Triángulo de Pascal ===\n")


def triangulo_pascal_filas(n):
    """
    Generates the first n rows of Pascal's Triangle.
    Complexity: O(n²)
    """
    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)  # Each row starts and ends with 1
        for j in range(1, i):
            # Each inner value = sum of the two values above
            fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)
    return triangulo


def triangulo_pascal_imprimir(n):
    """Prints Pascal's Triangle in visual form."""
    triangulo = triangulo_pascal_filas(n)
    ancho_maximo = len(' '.join(map(str, triangulo[-1])))
    for fila in triangulo:
        fila_str = ' '.join(map(str, fila))
        print(fila_str.center(ancho_maximo))


def triangulo_pascal_coeficiente(n, k):
    """
    Binomial coefficient C(n, k) = n! / (k! * (n-k)!).
    """
    if k > n or k < 0:
        return 0
    if k > n - k:
        k = n - k
    resultado = 1
    for i in range(k):
        resultado = resultado * (n - i) // (i + 1)
    return resultado


def triangulo_pascal_fila_n(n):
    """Generates only row n of Pascal's Triangle."""
    fila = [1]
    for k in range(n):
        siguiente = fila[k] * (n - k) // (k + 1)
        fila.append(siguiente)
    return fila


if __name__ == "__main__":
    print("Triángulo de Pascal (10 filas):")
    triangulo_pascal_imprimir(10)
    print(f"\nCoeficiente binomial C(5, 2) = {triangulo_pascal_coeficiente(5, 2)}")
    print(f"Fila 5 del Triángulo de Pascal: {triangulo_pascal_fila_n(5)}")
