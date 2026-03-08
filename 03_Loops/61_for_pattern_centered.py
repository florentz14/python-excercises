# -------------------------------------------------
# File Name: 61_for_pattern_centered.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Centered number pyramid.
# -------------------------------------------------

print("Pirámide Centrada con Números")
print("=" * 40)

size = 5

for i in range(1, size + 1):
    # Leading spaces to center
    for space in range(size - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
