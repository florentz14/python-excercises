# -------------------------------------------------
# File Name: 01_list.py
# Author: Florentino Báez
# Date: 12_Stacks
# Description: Stack with list (LIFO). append()=push, pop()=pop. Last in, first out.
# -------------------------------------------------

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
