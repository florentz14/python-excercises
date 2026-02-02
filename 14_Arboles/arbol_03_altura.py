"""
Árboles - Ejemplo 3: Altura y tamaño de un árbol binario
==========================================================
Tema: 14_Arboles
Descripción: altura(nodo) = 1 + max(altura(izq), altura(der)); tamaño = número de nodos.
"""


class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho


def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))


def tamaño(nodo):
    if nodo is None:
        return 0
    return 1 + tamaño(nodo.izquierdo) + tamaño(nodo.derecho)


# Árbol:    1
#          / \
#         2   3
#        /
#       4
raiz = Nodo(1, Nodo(2, Nodo(4)), Nodo(3))

print("Altura:", altura(raiz))   # 3
print("Tamaño (nº nodos):", tamaño(raiz))  # 4
