"""For loop: Pyramid of stars.
Prints rows of asterisks forming a pyramid.
"""
# Author: Florentino Báez


print("Pirámide de Asteriscos")
print("=" * 30)

rows = 5

# Outer loop: each row
for i in range(1, rows + 1):
    # Inner loop: print i asterisks
    for j in range(i):
        print("*", end=" ")
    print()
