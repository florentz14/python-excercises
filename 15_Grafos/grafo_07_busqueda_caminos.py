"""
15_Grafos - Búsqueda de caminos y componentes conexas
======================================================
GrafoCompleto: buscar_camino (BFS), todos_los_caminos, componentes_conexas.
"""

from collections import deque

from grafo_05_lista_adyacencia import GrafoListaAdyacencia


class GrafoCompleto(GrafoListaAdyacencia):
    """Grafo con algoritmos de búsqueda de caminos."""

    def buscar_camino(self, inicio, destino):
        """Busca un camino entre dos nodos usando BFS."""
        if inicio == destino:
            return [inicio]
        visitados = set()
        cola = deque([(inicio, [inicio])])
        visitados.add(inicio)

        while cola:
            nodo, camino = cola.popleft()
            for vecino, _ in self.grafo[nodo]:
                if vecino == destino:
                    return camino + [vecino]
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        return None

    def todos_los_caminos(self, inicio, destino):
        """Encuentra todos los caminos entre dos nodos."""

        def _buscar_caminos(nodo_actual, dest, visitados, camino_actual):
            visitados.add(nodo_actual)
            camino_actual.append(nodo_actual)
            if nodo_actual == dest:
                caminos.append(camino_actual.copy())
            else:
                for vecino, _ in self.grafo[nodo_actual]:
                    if vecino not in visitados:
                        _buscar_caminos(vecino, dest, visitados, camino_actual)
            camino_actual.pop()
            visitados.remove(nodo_actual)

        caminos = []
        _buscar_caminos(inicio, destino, set(), [])
        return caminos

    def componentes_conexas(self):
        """Encuentra todas las componentes conexas."""
        visitados = set()
        componentes = []
        for nodo in self.grafo:
            if nodo not in visitados:
                componente = self.bfs(nodo)
                componentes.append(componente)
                visitados.update(componente)
        return componentes


if __name__ == "__main__":
    print("=== Búsqueda de caminos ===\n")
    grafo = GrafoCompleto(dirigido=False)
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "E")

    print(f"Camino de A a E: {grafo.buscar_camino('A', 'E')}")
    print(f"Todos los caminos de A a D: {grafo.todos_los_caminos('A', 'D')}")
    print(f"Componentes conexas: {grafo.componentes_conexas()}")
