# -------------------------------------------------
# File Name: 71_while_factorial_input.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Factorial with input.
# -------------------------------------------------

print("=" * 40)
print("While #5 – Factorial (with input)")
print("=" * 40)

n = int(input("Enter a number: "))

fact = 1
k = 1

while k <= n:
    fact *= k
    k += 1

print("Factorial:", fact)
print("=" * 40)
