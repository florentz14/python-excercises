# -------------------------------------------------
# File Name: 13_map.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: map() — Apply a Function to Every Element.
#              map(func, iterable) returns an iterator that
#              applies func to each item. Wrap with list()
#              to get a list. Works with lambda, built-in
#              methods, or user-defined functions.
# -------------------------------------------------

print("=== map — apply function ===")
numeros = [1, 2, 3, 4, 5]

# Lambda squares each number
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Numbers: {numeros}")
print(f"Squares (map): {cuadrados}")

print("\n=== More examples ===")
nombres = ["ana", "juan", "pedro"]

# Pass a built-in method directly (str.upper)
mayusculas = list(map(str.upper, nombres))
print(f"Names: {nombres}")
print(f"Uppercase: {mayusculas}")

# map with a named function
def duplicar(x):
    """Return x multiplied by 2."""
    return x * 2

numeros = [1, 2, 3, 4, 5]
duplicados = list(map(duplicar, numeros))
print(f"Doubled: {duplicados}")
