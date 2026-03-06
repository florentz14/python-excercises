"""While loop: Sum 1 to 5.
Accumulates the sum using a counter and condition.
"""
# Author: Florentino Báez


count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

print("Total:", total)
