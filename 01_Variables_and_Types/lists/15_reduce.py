# -------------------------------------------------
# File Name: 15_reduce.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: reduce() — Reduce a List to a Single Value.
#              reduce(func, iterable) applies func cumulatively
#              to pairs of elements, left to right, reducing
#              the iterable to one value. Imported from
#              functools.
# -------------------------------------------------

from functools import reduce

print("=== reduce — fold to a single value ===")
numeros = [1, 2, 3, 4, 5]

# Sum all elements: ((((1+2)+3)+4)+5)
suma = reduce(lambda x, y: x + y, numeros)

# Multiply all elements: ((((1*2)*3)*4)*5)
producto = reduce(lambda x, y: x * y, numeros)

print(f"Numbers: {numeros}")
print(f"Sum (reduce): {suma}")
print(f"Product (reduce): {producto}")

print("\n=== More examples ===")
# Find maximum by keeping the larger of each pair
maximo = reduce(lambda x, y: x if x > y else y, numeros)

# Find minimum by keeping the smaller of each pair
minimo = reduce(lambda x, y: x if x < y else y, numeros)
print(f"Max: {maximo}")
print(f"Min: {minimo}")

# Concatenate strings
palabras = ["Hola", " ", "mundo", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print(f"Words: {palabras}")
print(f"Sentence: {frase}")
