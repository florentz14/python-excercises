# -------------------------------------------------
# File Name: 52_for_pattern_pyramid.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Pyramid of stars.
# -------------------------------------------------

print("Pirámide de Asteriscos")
print("=" * 30)

rows = 5

# Outer loop: each row
for i in range(1, rows + 1):
    # Inner loop: print i asterisks
    for j in range(i):
        print("*", end=" ")
    print()
