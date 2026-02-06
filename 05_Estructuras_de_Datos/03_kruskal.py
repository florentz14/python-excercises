# Archivo: 42_03_kruskal.py
# Descripción: Algoritmo de Kruskal para Minimum Spanning Tree (greedy)

print("=== 3. Algoritmo de Kruskal (MST) ===\n")


class UnionFind:
    """Estructura Union-Find para Kruskal."""

    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1
        return True


def kruskal(nodos, aristas):
    """
    Minimum Spanning Tree con Kruskal.
    Estrategia: Ordenar aristas por peso y agregar las que no formen ciclos.
    Complejidad: O(E log E)
    """
    aristas.sort(key=lambda x: x[2])
    uf = UnionFind(nodos)
    mst = []
    peso_total = 0

    for u, v, peso in aristas:
        if uf.unir(u, v):
            mst.append((u, v, peso))
            peso_total += peso
            if len(mst) == nodos - 1:
                break

    return mst, peso_total


if __name__ == "__main__":
    nodos_kruskal = 4
    aristas_kruskal = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    print(f"Grafo con {nodos_kruskal} nodos y {len(aristas_kruskal)} aristas:")
    for u, v, peso in aristas_kruskal:
        print(f"  {u} --{peso}-- {v}")

    mst, peso_total = kruskal(nodos_kruskal, aristas_kruskal)
    print(f"\nMinimum Spanning Tree (peso total: {peso_total}):")
    for u, v, peso in mst:
        print(f"  {u} --{peso}-- {v}")
