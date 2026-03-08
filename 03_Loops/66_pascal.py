# -------------------------------------------------
# File Name: 66_pascal.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Pascal's triangle.
# -------------------------------------------------

print("=" * 50)
print("TRIÁNGULO DE PASCAL")
print("=" * 50)

# Validate input: 1-15 rows
while True:
    try:
        rows = int(input("\n¿Cuántas filas del triángulo de Pascal deseas? (1-15): "))

        if rows < 1:
            print("Por favor, ingresa un número mayor que 0")
            continue

        if rows > 15:
            print("Por favor, ingresa un número máximo de 15")
            continue

        break

    except ValueError:
        print("Por favor, ingresa un número válido")

print(f"\nTriángulo de Pascal ({rows} filas)")
print("=" * 50)

# Each row in Pascal's triangle
for i in range(rows):
    # Leading spaces to center
    for space in range(rows - i - 1):
        print(" ", end="  ")

    # Binomial coefficient: C(i,j) = prev * (i-j) / (j+1)
    number = 1
    for j in range(i + 1):
        print(number, end="  ")
        number = number * (i - j) // (j + 1)

    print()

print("=" * 50)
