# -------------------------------------------------
# File Name: 02_deque.py
# Author: Florentino Báez
# Date: 13_Queues
# Description: Queue with collections.deque. append and popleft. O(1) at both ends.
# -------------------------------------------------

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
