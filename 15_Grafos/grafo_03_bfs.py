"""
Grafos - Ejemplo 3: BFS (recorrido en anchura)
===============================================
Tema: 15_Grafos
Descripción: Recorrer el grafo desde un vértice con cola (niveles).
"""

from collections import deque


def bfs(grafo, inicio):
    """BFS desde 'inicio'. Devuelve orden de visita."""
    visitado = {inicio}
    cola = deque([inicio])
    resultado = []

    while cola:
        v = cola.popleft()
        resultado.append(v)
        for w in grafo.get(v, []):
            if w not in visitado:
                visitado.add(w)
                cola.append(w)

    return resultado


# Grafo: 0 -- 1 -- 3
#         \   |
#           - 2
grafo = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}

print("BFS desde 0:", bfs(grafo, 0))  # [0, 1, 2, 3] (o [0, 2, 1, 3] según orden)
print("BFS desde 3:", bfs(grafo, 3))  # [3, 1, 0, 2]
