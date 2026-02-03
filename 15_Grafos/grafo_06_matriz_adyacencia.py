"""
15_Grafos - Grafo con matriz de adyacencia
===========================================
GrafoMatrizAdyacencia: representación con matriz, nodos con índices.
"""


class GrafoMatrizAdyacencia:
    """Grafo implementado con matriz de adyacencia."""

    def __init__(self, num_nodos, dirigido=False):
        self.num_nodos = num_nodos
        self.dirigido = dirigido
        self.matriz = [[0] * num_nodos for _ in range(num_nodos)]
        self.nodos = {}
        self.indices = {}
        self.contador = 0

    def agregar_nodo(self, nombre):
        """Agrega un nodo al grafo."""
        if nombre not in self.nodos:
            self.nodos[nombre] = self.contador
            self.indices[self.contador] = nombre
            self.contador += 1

    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista al grafo."""
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        i = self.nodos[origen]
        j = self.nodos[destino]
        self.matriz[i][j] = peso
        if not self.dirigido:
            self.matriz[j][i] = peso

    def imprimir_matriz(self):
        """Imprime la matriz de adyacencia."""
        print("Matriz de adyacencia:")
        print("   ", end="")
        for i in range(self.contador):
            print(f"{self.indices[i]:4s}", end="")
        print()
        for i in range(self.contador):
            print(f"{self.indices[i]:3s}", end=" ")
            for j in range(self.contador):
                print(f"{self.matriz[i][j]:4d}", end="")
            print()

    def obtener_vecinos(self, nodo):
        """Obtiene los vecinos de un nodo."""
        if nodo not in self.nodos:
            return []
        i = self.nodos[nodo]
        vecinos = []
        for j in range(self.contador):
            if self.matriz[i][j] != 0:
                vecinos.append((self.indices[j], self.matriz[i][j]))
        return vecinos


if __name__ == "__main__":
    print("=== Grafo con matriz de adyacencia ===\n")
    grafo = GrafoMatrizAdyacencia(5, dirigido=False)
    grafo.agregar_arista("A", "B", 1)
    grafo.agregar_arista("A", "C", 1)
    grafo.agregar_arista("B", "D", 1)
    grafo.agregar_arista("C", "D", 1)
    grafo.agregar_arista("D", "E", 1)

    grafo.imprimir_matriz()
    print(f"Vecinos de 'A': {grafo.obtener_vecinos('A')}")
