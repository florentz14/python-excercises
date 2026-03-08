# -------------------------------------------------
# File Name: 57_for_pattern_square.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Square pattern.
# -------------------------------------------------

print("Patrón de Cuadrado")
print("=" * 30)

size = 5

# Rows
for i in range(size):
    # Columns
    for j in range(size):
        print("*", end=" ")
    print()
