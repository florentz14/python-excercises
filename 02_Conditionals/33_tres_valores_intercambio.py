# -------------------------------------------------
# File Name: 33_tres_valores_intercambio.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Swap 3 values + max, min, average
# -------------------------------------------------

a = float(input("Valor 1: "))
b = float(input("Valor 2: "))
c = float(input("Valor 3: "))

print(f"\nOriginal: a={a}, b={b}, c={c}")

# Intercambio (rotar): a -> b, b -> c, c -> a
temp = a
a = b
b = c
c = temp
print(f"Después de rotar: a={a}, b={b}, c={c}")

# Mayor
if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c
print(f"Mayor: {mayor}")

# Menor
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c
print(f"Menor: {menor}")

# Promedio
promedio = (a + b + c) / 3
print(f"Promedio: {promedio:.2f}")
