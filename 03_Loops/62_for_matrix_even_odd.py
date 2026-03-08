# -------------------------------------------------
# File Name: 62_for_matrix_even_odd.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Classify matrix as even/odd.
# -------------------------------------------------

print("Clasificar Matriz 2D en Pares e Impares")
print("=" * 45)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_numbers = []
odd_numbers = []

print("Matriz:")
for row in matrix:
    print(row)

print("\nClasificando elementos...")

for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

print(f"\nNúmeros pares: {even_numbers}")
print(f"Números impares: {odd_numbers}")
print(f"Total de pares: {len(even_numbers)}")
print(f"Total de impares: {len(odd_numbers)}")
