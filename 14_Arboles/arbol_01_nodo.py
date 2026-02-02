"""
Árboles - Ejemplo 1: Nodo de árbol binario
===========================================
Tema: 14_Arboles
Descripción: Clase Nodo con valor, izquierdo y derecho.
"""


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
