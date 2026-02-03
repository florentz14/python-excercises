"""
15_Grafos - Grafo ponderado: camino mínimo y árbol de expansión mínima
=======================================================================
GrafoPonderado: camino_minimo (Dijkstra), arbol_expansion_minima (Prim).
"""

from grafo_05_lista_adyacencia import GrafoListaAdyacencia


class GrafoPonderado(GrafoListaAdyacencia):
    """Grafo con operaciones para pesos: camino mínimo y MST."""

    def camino_minimo(self, inicio, destino):
        """Camino mínimo entre inicio y destino (Dijkstra con reconstrucción)."""
        distancias = {nodo: float("inf") for nodo in self.obtener_nodos()}
        distancias[inicio] = 0
        padres = {}
        visitados = set()

        while len(visitados) < len(distancias):
            candidatos = [
                (n, d) for n, d in distancias.items() if n not in visitados
            ]
            if not candidatos:
                break
            nodo_actual = min(candidatos, key=lambda x: x[1])[0]
            if distancias[nodo_actual] == float("inf"):
                break
            visitados.add(nodo_actual)
            for vecino, peso in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    nueva = distancias[nodo_actual] + peso
                    if nueva < distancias[vecino]:
                        distancias[vecino] = nueva
                        padres[vecino] = nodo_actual

        if destino not in padres and inicio != destino:
            return None
        camino = []
        nodo = destino
        while nodo is not None:
            camino.append(nodo)
            nodo = padres.get(nodo)
        camino.reverse()
        return camino if camino and camino[0] == inicio else None

    def arbol_expansion_minima(self):
        """Árbol de expansión mínima (algoritmo de Prim)."""
        nodos = self.obtener_nodos()
        if not nodos:
            return []
        inicio = nodos[0]
        visitados = {inicio}
        aristas_mst = []

        while len(visitados) < len(nodos):
            min_arista = None
            min_peso = float("inf")
            for nodo in visitados:
                for vecino, peso in self.obtener_vecinos(nodo):
                    if vecino not in visitados and peso < min_peso:
                        min_peso = peso
                        min_arista = (nodo, vecino, peso)
            if min_arista:
                aristas_mst.append(min_arista)
                visitados.add(min_arista[1])
        return aristas_mst


if __name__ == "__main__":
    print("=== Grafo ponderado: camino mínimo y MST ===\n")
    grafo = GrafoPonderado(dirigido=False)
    grafo.agregar_arista("A", "B", 4)
    grafo.agregar_arista("A", "C", 2)
    grafo.agregar_arista("B", "C", 1)
    grafo.agregar_arista("B", "D", 5)
    grafo.agregar_arista("C", "D", 8)

    print(f"Camino mínimo de A a D: {grafo.camino_minimo('A', 'D')}")
    print(f"Árbol de expansión mínima: {grafo.arbol_expansion_minima()}")
