"""
Listas - Ejemplo 11: List comprehension avanzado
=================================================
Comprehension básico, con condiciones múltiples y anidado (matriz).
"""

print("=== List comprehension basico ===")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Pares del 1 al 10: {pares}\n")

print("=== Comprehension con varias condiciones ===")
numeros = [x for x in range(1, 21) if x % 2 == 0 if x % 3 == 0]
print(f"Divisibles por 2 y 3: {numeros}\n")

print("=== Comprehension anidado (matriz) ===")
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")
