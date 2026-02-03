"""
14_Arboles - Árbol N-ario (árbol general)
==========================================
NodoNario, ArbolNario: nodos con múltiples hijos; DFS y BFS.
"""

from collections import deque


class NodoNario:
    """Nodo de un árbol n-ario (múltiples hijos)."""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        """Agrega un hijo al nodo."""
        self.hijos.append(hijo)

    def __str__(self):
        return str(self.valor)


class ArbolNario:
    """Árbol n-ario (árbol general)."""

    def __init__(self, valor_raiz=None):
        if valor_raiz is not None:
            self.raiz = NodoNario(valor_raiz)
        else:
            self.raiz = None

    def recorrido_profundidad(self):
        """Recorrido en profundidad (DFS)."""
        if self.raiz is None:
            return []
        resultado = []
        self._dfs(self.raiz, resultado)
        return resultado

    def _dfs(self, nodo, resultado):
        """Recorrido en profundidad recursivo."""
        resultado.append(nodo.valor)
        for hijo in nodo.hijos:
            self._dfs(hijo, resultado)

    def recorrido_anchura(self):
        """Recorrido en anchura (BFS)."""
        if self.raiz is None:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            cola.extend(nodo.hijos)
        return resultado


if __name__ == "__main__":
    print("=== Árbol N-ario (general) ===\n")
    arbol = ArbolNario(1)
    nodo2 = NodoNario(2)
    nodo3 = NodoNario(3)
    nodo4 = NodoNario(4)
    nodo5 = NodoNario(5)
    nodo6 = NodoNario(6)

    arbol.raiz.agregar_hijo(nodo2)
    arbol.raiz.agregar_hijo(nodo3)
    nodo2.agregar_hijo(nodo4)
    nodo2.agregar_hijo(nodo5)
    nodo3.agregar_hijo(nodo6)

    print("Estructura: 1 -> [2, 3], 2 -> [4, 5], 3 -> [6]")
    print(f"Recorrido en profundidad (DFS): {arbol.recorrido_profundidad()}")
    print(f"Recorrido en anchura (BFS):     {arbol.recorrido_anchura()}")
