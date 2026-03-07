# -------------------------------------------------
# File Name: 11_comprehension_avanzado.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Advanced List Comprehension.
#              Basic comprehension, multiple conditions,
#              and nested comprehension to build a matrix
#              (list of lists).
# -------------------------------------------------

print("=== Basic list comprehension ===")
# Square each number from 1 to 5
cuadrados = [x**2 for x in range(1, 6)]
print(f"Squares from 1 to 5: {cuadrados}")

# Filter: keep only even numbers from 1 to 10
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers from 1 to 10: {pares}\n")

print("=== Comprehension with multiple conditions ===")
# Multiple 'if' clauses act as AND (both must be true)
numeros = [x for x in range(1, 21) if x % 2 == 0 if x % 3 == 0]
print(f"Divisible by 2 and 3: {numeros}\n")

print("=== Nested comprehension (matrix) ===")
# Outer loop generates rows, inner loop generates columns
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 Matrix:")
for fila in matriz:
    print(f"  {fila}")
