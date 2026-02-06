"""
Colas - Ejemplo 3: Clase Cola (con deque)
==========================================
Tema: 13_Colas
Descripción: Clase Cola con enqueue(), dequeue(), front() y empty().
"""

from collections import deque


class Cola:
    def __init__(self):
        self._datos = deque()

    def enqueue(self, x):
        self._datos.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("Dequeue en cola vacía")
        return self._datos.popleft()

    def front(self):
        if self.empty():
            raise IndexError("Front en cola vacía")
        return self._datos[0]

    def empty(self):
        return len(self._datos) == 0

    def __len__(self):
        return len(self._datos)


# --- Demo ---
if __name__ == "__main__":
    c = Cola()
    c.enqueue(10)
    c.enqueue(20)
    c.enqueue(30)
    print("Frente:", c.front())
    print("Dequeue:", c.dequeue())
    print("Dequeue:", c.dequeue())
    print("Vacía?", c.empty())
