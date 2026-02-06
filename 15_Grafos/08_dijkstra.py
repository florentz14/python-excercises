"""
15_Grafos - Algoritmo de Dijkstra (camino más corto)
=====================================================
Distancias mínimas desde un nodo origen en grafo con pesos no negativos.
"""

from grafo_05_lista_adyacencia import GrafoListaAdyacencia


def dijkstra(grafo, inicio):
    """Dijkstra: distancias mínimas desde 'inicio' a todos los nodos."""
    distancias = {nodo: float("inf") for nodo in grafo.obtener_nodos()}
    distancias[inicio] = 0
    visitados = set()

    while len(visitados) < len(distancias):
        nodo_actual = None
        min_distancia = float("inf")
        for nodo, distancia in distancias.items():
            if nodo not in visitados and distancia < min_distancia:
                min_distancia = distancia
                nodo_actual = nodo
        if nodo_actual is None:
            break
        visitados.add(nodo_actual)
        for vecino, peso in grafo.obtener_vecinos(nodo_actual):
            if vecino not in visitados:
                nueva = distancias[nodo_actual] + peso
                if nueva < distancias[vecino]:
                    distancias[vecino] = nueva
    return distancias


if __name__ == "__main__":
    print("=== Dijkstra (camino más corto) ===\n")
    grafo = GrafoListaAdyacencia(dirigido=False)
    grafo.agregar_arista("A", "B", 4)
    grafo.agregar_arista("A", "C", 2)
    grafo.agregar_arista("B", "C", 1)
    grafo.agregar_arista("B", "D", 5)
    grafo.agregar_arista("C", "D", 8)
    grafo.agregar_arista("C", "E", 10)
    grafo.agregar_arista("D", "E", 2)

    distancias = dijkstra(grafo, "A")
    print(f"Distancias más cortas desde 'A': {distancias}")
