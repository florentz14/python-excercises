"""For loop: 10x10 multiplication table.
Full multiplication grid from 1 to 10.
"""
# Author: Florentino Báez


print("Tabla de Multiplicación 10x10")
print("=" * 50)

# Outer loop: rows (1 to 10)
for i in range(1, 11):
    # Inner loop: columns (1 to 10)
    for j in range(1, 11):
        print(f"{i:2d} x {j:2d} = {i*j:3d}", end="  ")
    print()
