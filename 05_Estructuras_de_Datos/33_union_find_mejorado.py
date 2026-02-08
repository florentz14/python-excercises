# -------------------------------------------------
# File Name: 33_union_find_mejorado.py
# Author: Florentino Báez
# Date: Data Structures - Advanced Structures
# Description: Improved Union-Find (Disjoint Set Union).
#              Maintains disjoint sets with operations
#              find (with path compression) and union (with
#              union by rank). Amortized complexity: O(α(n))
#              ≈ constant. Useful for detecting cycles in graphs
#              and connected components.
# -------------------------------------------------

print("=== 4. Union-Find Mejorado ===\n")


class UnionFind:
    """
    Union-Find with path compression and union by rank.
    Complexity: O(α(n)) ≈ constant in practice.
    """

    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n
        self.tamaño = [1] * n
        self.num_componentes = n

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
            raiz_x, raiz_y = raiz_y, raiz_x
        self.padre[raiz_y] = raiz_x
        self.tamaño[raiz_x] += self.tamaño[raiz_y]
        if self.rango[raiz_x] == self.rango[raiz_y]:
            self.rango[raiz_x] += 1
        self.num_componentes -= 1
        return True

    def mismo_conjunto(self, x, y):
        return self.encontrar(x) == self.encontrar(y)

    def tamaño_componente(self, x):
        return self.tamaño[self.encontrar(x)]

    def obtener_componentes(self):
        componentes = {}
        for i in range(len(self.padre)):
            raiz = self.encontrar(i)
            if raiz not in componentes:
                componentes[raiz] = []
            componentes[raiz].append(i)
        return componentes


if __name__ == "__main__":
    uf = UnionFind(10)
    print("Uniendo elementos:")
    uniones = [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (1, 3)]
    for x, y in uniones:
        uf.unir(x, y)
        print(f"  Unir {x} y {y}: Componentes = {uf.num_componentes}")

    print(f"\nNúmero de componentes: {uf.num_componentes}")
    print(f"¿0 y 3 en mismo conjunto? {uf.mismo_conjunto(0, 3)}")
    print(f"Tamaño de componente de 0: {uf.tamaño_componente(0)}")
    print(f"Componentes: {uf.obtener_componentes()}")
