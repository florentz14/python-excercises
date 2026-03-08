# -------------------------------------------------
# File Name: 58_for_pattern_diagonal.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Diagonal pattern.
# -------------------------------------------------

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
