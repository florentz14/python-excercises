"""While loop: Running total 1 to 5.
Accumulates sum and prints counter with total each step.
"""
# Author: Florentino Báez


print("=" * 40)
print("While #3 – Running Total (1 to 5)")
print("=" * 40)

total = 0
i = 1

while i <= 5:
    total += i
    print("i:", i, "total:", total)
    i += 1

print("=" * 40)
