"""
15_Grafos - Ordenamiento topológico (DAG)
=========================================
Orden lineal de nodos en grafo dirigido acíclico.
"""

from collections import deque, defaultdict

from grafo_05_lista_adyacencia import GrafoListaAdyacencia


def ordenamiento_topologico(grafo):
    """Orden topológico para DAG. Devuelve None si hay ciclo."""
    grados_entrada = defaultdict(int)
    for nodo in grafo.obtener_nodos():
        for vecino, _ in grafo.obtener_vecinos(nodo):
            grados_entrada[vecino] += 1

    cola = deque(
        [nodo for nodo in grafo.obtener_nodos() if grados_entrada[nodo] == 0]
    )
    resultado = []

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        for vecino, _ in grafo.obtener_vecinos(nodo):
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)

    if len(resultado) != len(grafo.obtener_nodos()):
        return None
    return resultado


if __name__ == "__main__":
    print("=== Ordenamiento topológico (DAG) ===\n")
    grafo = GrafoListaAdyacencia(dirigido=True)
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "D")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "E")

    orden = ordenamiento_topologico(grafo)
    print(f"Orden topológico: {orden}")
