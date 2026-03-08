# -------------------------------------------------
# File Name: 01_node.py
# Author: Florentino Báez
# Date: 14_Trees
# Description: Binary tree node class with value, left, and right children.
# -------------------------------------------------

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho


# Construir árbol:      1
#                      / \
#                     2   3
#                    /
#                   4
raiz = Nodo(1, Nodo(2, Nodo(4)), Nodo(3))

print("Raíz:", raiz.valor)
print("Izq:", raiz.izquierdo.valor)
print("Der:", raiz.derecho.valor)
print("Izq.Izq:", raiz.izquierdo.izquierdo.valor)
