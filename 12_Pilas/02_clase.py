"""
Pilas - Ejemplo 2: Clase Pila
==============================
Tema: 12_Pilas
Descripción: Clase que encapsula push(), pop(), peek() y empty().
"""


class Pila:
    def __init__(self):
        self._datos = []

    def push(self, x):
        self._datos.append(x)

    def pop(self):
        if self.empty():
            raise IndexError("Pop en pila vacía")
        return self._datos.pop()

    def peek(self):
        if self.empty():
            raise IndexError("Peek en pila vacía")
        return self._datos[-1]

    def empty(self):
        return len(self._datos) == 0

    def __len__(self):
        return len(self._datos)


# --- Demo ---
if __name__ == "__main__":
    p = Pila()
    p.push("A")
    p.push("B")
    p.push("C")
    print("Tope:", p.peek())
    print("Pop:", p.pop())
    print("Pop:", p.pop())
    print("Vacía?", p.empty())
