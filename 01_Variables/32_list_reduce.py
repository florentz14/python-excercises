# Listas - reduce(): reducir a un valor
from functools import reduce

print("=== reduce - reducir a un valor ===")
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
producto = reduce(lambda x, y: x * y, numeros)
print(f"Numeros: {numeros}")
print(f"Suma (reduce): {suma}")
print(f"Producto (reduce): {producto}")

# Más ejemplos de reduce
print("\n=== Más ejemplos ===")
maximo = reduce(lambda x, y: x if x > y else y, numeros)
minimo = reduce(lambda x, y: x if x < y else y, numeros)
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# Concatenar strings
palabras = ["Hola", " ", "mundo", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print(f"Palabras: {palabras}")
print(f"Frase: {frase}")
