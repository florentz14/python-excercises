"""For loop: Diagonal pattern.
Prints X on main diagonal, dots elsewhere.
"""
# Author: Florentino Báez


print("Patrón de Diagonal")
print("=" * 30)

size = 5

for i in range(size):
    for j in range(size):
        # Main diagonal: row index equals column index
        if i == j:
            print("X", end=" ")
        else:
            print(".", end=" ")
    print()
