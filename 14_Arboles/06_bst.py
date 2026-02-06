"""
14_Arboles - Árbol binario de búsqueda (BST)
=============================================
ArbolBST: es_bst, encontrar_minimo, encontrar_maximo.
"""

from arbol_05_recorridos import ArbolRecorridos


class ArbolBST(ArbolRecorridos):
    """Árbol binario de búsqueda completo."""

    def es_bst(self):
        """Verifica si el árbol es un BST válido."""
        return self._es_bst_recursivo(self.raiz, float("-inf"), float("inf"))

    def _es_bst_recursivo(self, nodo, minimo, maximo):
        """Verifica recursivamente si es BST."""
        if nodo is None:
            return True
        if nodo.valor <= minimo or nodo.valor >= maximo:
            return False
        return self._es_bst_recursivo(
            nodo.izquierda, minimo, nodo.valor
        ) and self._es_bst_recursivo(nodo.derecha, nodo.valor, maximo)

    def encontrar_minimo(self):
        """Encuentra el valor mínimo en el árbol."""
        if self.raiz is None:
            return None
        return self._encontrar_minimo_recursivo(self.raiz)

    def _encontrar_minimo_recursivo(self, nodo):
        if nodo.izquierda is None:
            return nodo.valor
        return self._encontrar_minimo_recursivo(nodo.izquierda)

    def encontrar_maximo(self):
        """Encuentra el valor máximo en el árbol."""
        if self.raiz is None:
            return None
        return self._encontrar_maximo_recursivo(self.raiz)

    def _encontrar_maximo_recursivo(self, nodo):
        if nodo.derecha is None:
            return nodo.valor
        return self._encontrar_maximo_recursivo(nodo.derecha)


if __name__ == "__main__":
    print("=== Árbol binario de búsqueda (BST) ===\n")
    arbol = ArbolBST()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    print(f"¿Es BST válido? {arbol.es_bst()}")
    print(f"Valor mínimo: {arbol.encontrar_minimo()}")
    print(f"Valor máximo: {arbol.encontrar_maximo()}")
