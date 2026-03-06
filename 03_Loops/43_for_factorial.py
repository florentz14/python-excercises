"""For loop: Factorial.
Computes n! by multiplying 1 through n.
"""
# Author: Florentino Báez


number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"Factorial of {number} is {factorial}")
