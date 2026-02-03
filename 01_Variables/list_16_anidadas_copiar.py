"""
Listas - Ejemplo 16: Listas anidadas y copiar (shallow / deep)
================================================================
Matriz como lista de listas; copy() vs copy.deepcopy().
"""

print("=== Listas anidadas (matriz) ===")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")
print(f"Elemento [1][2]: {matriz[1][2]}\n")

print("=== Copiar listas ===")
import copy
original = [1, 2, 3, [4, 5]]
copia_superficial = original.copy()
copia_profunda = copy.deepcopy(original)
original[3].append(6)
print(f"Original: {original}")
print(f"Copia superficial (se ve afectada): {copia_superficial}")
print(f"Copia profunda (no cambia): {copia_profunda}")
