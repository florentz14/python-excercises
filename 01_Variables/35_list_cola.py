# Listas como Cola (Queue - FIFO: First In, First Out)
from collections import deque

print("=== Lista como cola (FIFO) ===")
print("Usar deque para eficiencia: append() para agregar, popleft() para sacar")
print()

cola = deque()
print(f"Cola vacía: {cola}")

# Enqueue (agregar al final)
cola.append(1)
cola.append(2)
cola.append(3)
print(f"Después de append(1), append(2), append(3): {cola}")

# Dequeue (sacar del frente)
primero = cola.popleft()
print(f"popleft() retorna: {primero}")
print(f"Cola después de popleft: {cola}")

# Más operaciones
cola.append(4)
cola.append(5)
print(f"Después de append(4), append(5): {cola}")

print(f"popleft(): {cola.popleft()}")
print(f"popleft(): {cola.popleft()}")
print(f"Cola final: {cola}")

# Peek (ver el frente sin sacar)
print(f"\nVer el frente sin sacar (peek): cola[0] = {cola[0]}")

# También se puede agregar al frente
cola.appendleft(0)
print(f"Después de appendleft(0): {cola}")
