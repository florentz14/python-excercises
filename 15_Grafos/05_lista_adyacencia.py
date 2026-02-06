"""
15_Grafos - Grafo con lista de adyacencia
=========================================
GrafoListaAdyacencia: dirigido/no dirigido, BFS, DFS, DFS iterativo.
"""

from collections import deque, defaultdict


class GrafoListaAdyacencia:
    """Grafo implementado con lista de adyacencia."""

    def __init__(self, dirigido=False):
        self.grafo = defaultdict(list)
        self.dirigido = dirigido

    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista al grafo."""
        self.grafo[origen].append((destino, peso))
        if not self.dirigido:
            self.grafo[destino].append((origen, peso))

    def obtener_vecinos(self, nodo):
        """Obtiene los vecinos de un nodo."""
        return self.grafo[nodo]

    def obtener_nodos(self):
        """Obtiene todos los nodos del grafo."""
        return list(self.grafo.keys())

    def imprimir_grafo(self):
        """Imprime el grafo."""
        for nodo in self.grafo:
            print(f"{nodo}: {self.grafo[nodo]}")

    def bfs(self, inicio):
        """Recorrido en anchura (Breadth First Search)."""
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        resultado = []

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def dfs(self, inicio):
        """Recorrido en profundidad (Depth First Search)."""
        visitados = set()
        resultado = []

        def _dfs_recursivo(nodo):
            visitados.add(nodo)
            resultado.append(nodo)
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    _dfs_recursivo(vecino)

        _dfs_recursivo(inicio)
        return resultado

    def dfs_iterativo(self, inicio):
        """DFS iterativo usando pila."""
        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            nodo = pila.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                resultado.append(nodo)
                for vecino, _ in reversed(self.grafo[nodo]):
                    if vecino not in visitados:
                        pila.append(vecino)
        return resultado


if __name__ == "__main__":
    print("=== Grafo con lista de adyacencia ===\n")
    grafo = GrafoListaAdyacencia(dirigido=False)
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "E")

    print("Grafo (lista de adyacencia):")
    grafo.imprimir_grafo()
    print(f"\nBFS desde 'A': {grafo.bfs('A')}")
    print(f"DFS desde 'A': {grafo.dfs('A')}")
    print(f"DFS iterativo desde 'A': {grafo.dfs_iterativo('A')}")
