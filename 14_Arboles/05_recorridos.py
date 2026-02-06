"""
14_Arboles - Recorridos de árbol (preorden, inorden, postorden, por niveles)
=============================================================================
ArbolRecorridos: preorden, inorden, postorden, nivel orden (BFS).
"""

from collections import deque

from arbol_04_binario_basico import ArbolBinario, NodoArbol


class ArbolRecorridos(ArbolBinario):
    """Árbol binario con métodos de recorrido."""

    def recorrido_preorden(self):
        """Recorrido preorden: raíz, izquierda, derecha."""
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)

    def recorrido_inorden(self):
        """Recorrido inorden: izquierda, raíz, derecha."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

    def recorrido_postorden(self):
        """Recorrido postorden: izquierda, derecha, raíz."""
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierda, resultado)
            self._postorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    def recorrido_nivel_orden(self):
        """Recorrido por niveles (BFS - Breadth First Search)."""
        if self.raiz is None:
            return []

        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

        return resultado


if __name__ == "__main__":
    print("=== Recorridos de árbol ===\n")
    arbol = ArbolRecorridos()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    print(f"Preorden (raíz, izq, der):   {arbol.recorrido_preorden()}")
    print(f"Inorden (izq, raíz, der):   {arbol.recorrido_inorden()}")
    print(f"Postorden (izq, der, raíz): {arbol.recorrido_postorden()}")
    print(f"Nivel orden (BFS):           {arbol.recorrido_nivel_orden()}")
