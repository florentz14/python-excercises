"""
if.py - Ejemplo 1: Clasificar número (positivo, negativo, cero)
================================================================
Tema: Condicionales (02_Condicionales)
Descripción: if/elif/else para clasificar un número.
"""

print("Example 1: Number Classification")
print("-" * 40)
number = 15

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")
