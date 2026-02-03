"""
14_Arboles - Árbol binario básico
==================================
NodoArbol, ArbolBinario: insertar, buscar, altura, tamaño.
"""


class NodoArbol:
    """Nodo de un árbol binario."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return str(self.valor)


class ArbolBinario:
    """Árbol binario simple."""

    def __init__(self, valor_raiz=None):
        if valor_raiz is not None:
            self.raiz = NodoArbol(valor_raiz)
        else:
            self.raiz = None

    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        """Inserta recursivamente en el árbol."""
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        """Busca recursivamente en el árbol."""
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        """Calcula la altura recursivamente."""
        if nodo is None:
            return -1
        return 1 + max(
            self._altura_recursiva(nodo.izquierda),
            self._altura_recursiva(nodo.derecha),
        )

    def tamaño(self):
        """Calcula el número de nodos."""
        return self._tamaño_recursivo(self.raiz)

    def _tamaño_recursivo(self, nodo):
        """Calcula el tamaño recursivamente."""
        if nodo is None:
            return 0
        return (
            1
            + self._tamaño_recursivo(nodo.izquierda)
            + self._tamaño_recursivo(nodo.derecha)
        )


if __name__ == "__main__":
    print("=== Árbol binario básico ===\n")
    arbol = ArbolBinario()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    print(f"Valores insertados: {valores}")
    print(f"Buscar 40: {arbol.buscar(40)}")
    print(f"Buscar 100: {arbol.buscar(100)}")
    print(f"Altura del árbol: {arbol.altura()}")
    print(f"Tamaño del árbol: {arbol.tamaño()}")
