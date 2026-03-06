"""For loop: Interactive multiplication table.
User chooses which table (1-12) to display; validates input.
"""
# Author: Florentino Báez


print("=" * 50)
print("TABLA DE MULTIPLICACIÓN INTERACTIVA")
print("=" * 50)

# Validate input until valid number 1-12
while True:
    try:
        number = int(input("\n¿Qué tabla de multiplicación deseas? (1-12): "))

        if number < 1 or number > 12:
            print("Por favor, ingresa un número entre 1 y 12")
            continue

        break

    except ValueError:
        print("Por favor, ingresa un número válido")

print(f"\nTabla de Multiplicación del {number}")
print("=" * 40)

for i in range(1, 13):
    resultado = number * i
    print(f"{number} x {i:2d} = {resultado:3d}")

print("=" * 40)
