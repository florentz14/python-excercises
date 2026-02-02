"""
Árboles - Ejemplo 2: Recorridos (inorden, preorden, postorden)
===============================================================
Tema: 14_Arboles
Descripción: Recorrer árbol binario: inorden (izq, raíz, der), preorden (raíz, izq, der), postorden (izq, der, raíz).
"""


class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho


def inorden(nodo):
    if nodo is None:
        return []
    return inorden(nodo.izquierdo) + [nodo.valor] + inorden(nodo.derecho)


def preorden(nodo):
    if nodo is None:
        return []
    return [nodo.valor] + preorden(nodo.izquierdo) + preorden(nodo.derecho)


def postorden(nodo):
    if nodo is None:
        return []
    return postorden(nodo.izquierdo) + postorden(nodo.derecho) + [nodo.valor]


# Árbol:    1
#          / \
#         2   3
#        / \
#       4   5
raiz = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3))

print("Inorden (izq-raíz-der):", inorden(raiz))    # [4, 2, 5, 1, 3]
print("Preorden (raíz-izq-der):", preorden(raiz))  # [1, 2, 4, 5, 3]
print("Postorden (izq-der-raíz):", postorden(raiz))  # [4, 5, 2, 3, 1]
