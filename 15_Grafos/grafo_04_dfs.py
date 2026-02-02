"""
Grafos - Ejemplo 4: DFS (recorrido en profundidad)
===================================================
Tema: 15_Grafos
Descripción: Recorrer el grafo desde un vértice con pila o recursión.
"""

def dfs(grafo, inicio):
    """DFS desde 'inicio'. Devuelve orden de visita."""
    visitado = set()
    resultado = []

    def _dfs(v):
        visitado.add(v)
        resultado.append(v)
        for w in grafo.get(v, []):
            if w not in visitado:
                _dfs(w)

    _dfs(inicio)
    return resultado


# Grafo: 0 -- 1 -- 3
#         \   |
#           - 2
grafo = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}

print("DFS desde 0:", dfs(grafo, 0))  # [0, 1, 2, 3] (según orden de vecinos)
print("DFS desde 3:", dfs(grafo, 3))  # [3, 1, 0, 2]
