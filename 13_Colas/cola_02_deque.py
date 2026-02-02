"""
Colas - Ejemplo 2: Cola con collections.deque (FIFO)
=====================================================
Tema: 13_Colas
Descripción: deque: append = encolar, popleft() = desencolar; O(1) en ambos extremos.
"""

from collections import deque

cola = deque()

# Encolar
cola.append("A")
cola.append("B")
cola.append("C")
print("Cola:", list(cola))

# Desencolar (popleft = O(1))
primero = cola.popleft()
print("Desencolar:", primero, "→ Cola:", list(cola))
print("Desencolar:", cola.popleft(), "→ Cola:", list(cola))

# Ver el frente sin quitar
if cola:
    print("Frente:", cola[0])
