# -------------------------------------------------
# File Name: 32_par_impar_multiplo.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Even, odd, or multiple of 5
# -------------------------------------------------

n = int(input("Enter a number: "))

if n % 5 == 0:
    result = "Multiple of 5"
elif n % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f"{n} → {result}")
