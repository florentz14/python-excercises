"""
Listas - Ejemplo 13: map, filter y reduce
==========================================
Aplicar función (map), filtrar (filter), reducir a un valor (reduce).
"""

print("=== map - aplicar funcion ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Numeros: {numeros}")
print(f"Cuadrados (map): {cuadrados}\n")

print("=== filter - filtrar elementos ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Numeros: {numeros}")
print(f"Pares (filter): {pares}\n")

print("=== reduce - reducir a un valor ===")
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
producto = reduce(lambda x, y: x * y, numeros)
print(f"Numeros: {numeros}")
print(f"Suma (reduce): {suma}")
print(f"Producto (reduce): {producto}")
