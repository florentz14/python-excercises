"""
Grafos - Ejemplo 1: Grafo con lista de adyacencia
==================================================
Tema: 15_Grafos
Descripción: Grafo como dict: vértice → lista de vértices adyacentes.
"""

# Grafo no dirigido: 0 -- 1
#                     | \  |
#                     2 -- 3
grafo = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2],
}

print("Vértices:", list(grafo.keys()))
print("Adyacentes de 0:", grafo[0])
print("Adyacentes de 3:", grafo[3])

# Añadir vértice y arista
grafo[4] = [1]
grafo[1].append(4)
print("Tras añadir 4 y arista (1,4):", grafo)
