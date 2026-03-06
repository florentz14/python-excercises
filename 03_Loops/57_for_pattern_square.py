"""For loop: Square pattern.
Prints a 5x5 grid of asterisks.
"""
# Author: Florentino Báez


print("Patrón de Cuadrado")
print("=" * 30)

size = 5

# Rows
for i in range(size):
    # Columns
    for j in range(size):
        print("*", end=" ")
    print()
