"""
Pilas - Ejemplo 1: Pila con lista (LIFO)
========================================
Tema: 12_Pilas
Descripción: Usar lista como pila: append() = push, pop() = pop (último en entrar, primero en salir).
"""

pila = []

# Push: añadir al final
pila.append(1)
pila.append(2)
pila.append(3)
print("Después de push 1, 2, 3:", pila)

# Pop: quitar el último
top = pila.pop()
print("Pop:", top, "→ Pila:", pila)
print("Pop:", pila.pop(), "→ Pila:", pila)

# Ver el tope sin quitar
if pila:
    print("Tope (sin quitar):", pila[-1])
