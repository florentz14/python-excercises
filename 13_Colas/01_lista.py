"""
Colas - Ejemplo 1: Cola con lista (FIFO)
=========================================
Tema: 13_Colas
Descripción: Lista como cola: insert(0, x) = encolar al frente, pop() = desencolar al final (lento).
              Mejor usar collections.deque.
"""

cola = []

# Encolar: añadir al final
cola.append("A")
cola.append("B")
cola.append("C")
print("Cola:", cola)

# Desencolar: quitar el primero (pop(0) es O(n))
primero = cola.pop(0)
print("Desencolar:", primero, "→ Cola:", cola)
print("Desencolar:", cola.pop(0), "→ Cola:", cola)
