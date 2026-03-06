# -------------------------------------------------
# File Name: 14_filter.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: filter() — Keep Elements That Match a Condition.
#              filter(func, iterable) returns an iterator of
#              items for which func returns True. Works with
#              lambda or user-defined predicate functions.
# -------------------------------------------------

print("=== filter — keep matching elements ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda keeps only even numbers
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Numbers: {numeros}")
print(f"Even (filter): {pares}")

print("\n=== More examples ===")
# Keep only odd numbers
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Odd: {impares}")

# Keep numbers greater than 5
mayores_5 = list(filter(lambda x: x > 5, numeros))
print(f"Greater than 5: {mayores_5}")

# filter with a named predicate function
def es_positivo(x):
    """Return True if x is positive."""
    return x > 0

numeros = [-3, -1, 0, 2, 5, -4, 8]
positivos = list(filter(es_positivo, numeros))
print(f"Numbers: {numeros}")
print(f"Positive: {positivos}")
