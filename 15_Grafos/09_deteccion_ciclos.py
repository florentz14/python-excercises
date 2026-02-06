"""
15_Grafos - Detección de ciclos
================================
tiene_ciclo para grafos dirigidos y no dirigidos.
"""

from grafo_05_lista_adyacencia import GrafoListaAdyacencia


def tiene_ciclo(grafo, dirigido=True):
    """Indica si el grafo tiene al menos un ciclo."""
    if dirigido:
        return _tiene_ciclo_dirigido(grafo)
    return _tiene_ciclo_no_dirigido(grafo)


def _tiene_ciclo_no_dirigido(grafo):
    """Ciclos en grafo no dirigido (DFS con padre)."""
    visitados = set()

    def dfs_con_padre(nodo, padre):
        visitados.add(nodo)
        for vecino, _ in grafo.obtener_vecinos(nodo):
            if vecino not in visitados:
                if dfs_con_padre(vecino, nodo):
                    return True
            elif vecino != padre:
                return True
        return False

    for nodo in grafo.obtener_nodos():
        if nodo not in visitados:
            if dfs_con_padre(nodo, None):
                return True
    return False


def _tiene_ciclo_dirigido(grafo):
    """Ciclos en grafo dirigido (DFS con pila de recursión)."""
    visitados = set()
    en_recursion = set()

    def dfs(nodo):
        visitados.add(nodo)
        en_recursion.add(nodo)
        for vecino, _ in grafo.obtener_vecinos(nodo):
            if vecino not in visitados:
                if dfs(vecino):
                    return True
            elif vecino in en_recursion:
                return True
        en_recursion.remove(nodo)
        return False

    for nodo in grafo.obtener_nodos():
        if nodo not in visitados:
            if dfs(nodo):
                return True
    return False


if __name__ == "__main__":
    print("=== Detección de ciclos ===\n")
    grafo_ciclo = GrafoListaAdyacencia(dirigido=False)
    grafo_ciclo.agregar_arista("A", "B")
    grafo_ciclo.agregar_arista("B", "C")
    grafo_ciclo.agregar_arista("C", "A")
    print(f"Grafo con ciclo: {tiene_ciclo(grafo_ciclo, dirigido=False)}")

    grafo_sin = GrafoListaAdyacencia(dirigido=False)
    grafo_sin.agregar_arista("A", "B")
    grafo_sin.agregar_arista("B", "C")
    print(f"Grafo sin ciclo: {tiene_ciclo(grafo_sin, dirigido=False)}")
