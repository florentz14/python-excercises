"""For loop: Inverted triangle pattern.
Each row has decreasing number of columns.
"""
# Author: Florentino Báez


print("Triángulo Invertido")
print("=" * 30)

size = 5

# Rows from size down to 1
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
