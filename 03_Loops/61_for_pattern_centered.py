"""For loop: Centered number pyramid.
Numbers centered with leading spaces.
"""
# Author: Florentino Báez


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
