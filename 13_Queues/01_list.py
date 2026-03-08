# -------------------------------------------------
# File Name: 01_list.py
# Author: Florentino Báez
# Date: 13_Queues
# Description: Queue with list (FIFO). append() and pop(0). Better: use deque.
# -------------------------------------------------

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
