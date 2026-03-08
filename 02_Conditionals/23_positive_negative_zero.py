# -------------------------------------------------
# File Name: 23_positive_negative_zero.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Positive, negative, or zero
# -------------------------------------------------

numero = int(input("Enter a number: "))

if numero > 0:
    print(f"{numero} is positive")
elif numero < 0:
    print(f"{numero} is negative")
else:
    print("Zero")
