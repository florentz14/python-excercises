"""
Listas - Ejemplo 15: Listas como pila y como cola
==================================================
Pila: append + pop. Cola: deque con append y popleft().
"""

print("=== Lista como pila (LIFO) ===")
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(f"Pila despues de append: {pila}")
ultimo = pila.pop()
print(f"Ultimo (pop): {ultimo}")
print(f"Pila despues de pop: {pila}\n")

print("=== Lista como cola (FIFO) ===")
from collections import deque
cola = deque([1, 2, 3])
cola.append(4)
print(f"Cola: {cola}")
primero = cola.popleft()
print(f"Primero (popleft): {primero}")
print(f"Cola despues de popleft: {cola}")
