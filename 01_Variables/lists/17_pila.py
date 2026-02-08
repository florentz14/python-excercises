# Listas como Pila (Stack - LIFO: Last In, First Out)
print("=== Lista como pila (LIFO) ===")
print("Operaciones: append() para agregar, pop() para sacar")
print()

pila = []
print(f"Pila vacía: {pila}")

# Push (agregar al final)
pila.append(1)
pila.append(2)
pila.append(3)
print(f"Después de append(1), append(2), append(3): {pila}")

# Pop (sacar del final)
ultimo = pila.pop()
print(f"pop() retorna: {ultimo}")
print(f"Pila después de pop: {pila}")

# Más operaciones
pila.append(4)
pila.append(5)
print(f"Después de append(4), append(5): {pila}")

print(f"pop(): {pila.pop()}")
print(f"pop(): {pila.pop()}")
print(f"Pila final: {pila}")

# Peek (ver el tope sin sacar)
print(f"\nVer el tope sin sacar (peek): pila[-1] = {pila[-1]}")
