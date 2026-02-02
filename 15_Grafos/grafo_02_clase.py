"""
Grafos - Ejemplo 2: Clase Grafo (lista de adyacencia)
=====================================================
Tema: 15_Grafos
Descripción: Clase Grafo con add_vertice(), add_arista(), adyacentes().
"""


class Grafo:
    def __init__(self):
        self.ady = {}  # vértice -> set de vecinos

    def add_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = set()

    def add_arista(self, u, v):
        self.add_vertice(u)
        self.add_vertice(v)
        self.ady[u].add(v)
        self.ady[v].add(u)  # no dirigido

    def adyacentes(self, v):
        return self.ady.get(v, set())

    def vertices(self):
        return list(self.ady.keys())


# --- Demo ---
if __name__ == "__main__":
    g = Grafo()
    g.add_arista(0, 1)
    g.add_arista(0, 2)
    g.add_arista(1, 3)
    g.add_arista(2, 3)

    print("Vértices:", g.vertices())
    print("Adyacentes de 0:", g.adyacentes(0))
    print("Adyacentes de 3:", g.adyacentes(3))
