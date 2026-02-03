# Archivo: 48_03_fenwick_tree.py
# Descripción: Fenwick Tree (Binary Indexed Tree)

print("=== 3. Fenwick Tree (Binary Indexed Tree) ===\n")


class FenwickTree:
    """
    Fenwick Tree para sumas de prefijos.
    Complejidad: O(log n) consulta y actualización.
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.arbol = [0] * (self.n + 1)
        for i in range(self.n):
            self.actualizar(i, arr[i])

    def _lsb(self, x):
        return x & -x

    def actualizar(self, indice, delta):
        indice += 1
        while indice <= self.n:
            self.arbol[indice] += delta
            indice += self._lsb(indice)

    def consultar_prefijo(self, indice):
        indice += 1
        suma = 0
        while indice > 0:
            suma += self.arbol[indice]
            indice -= self._lsb(indice)
        return suma

    def consultar_rango(self, l, r):
        """Suma del rango [l, r] (inclusive)."""
        if l == 0:
            return self.consultar_prefijo(r)
        return self.consultar_prefijo(r) - self.consultar_prefijo(l - 1)


if __name__ == "__main__":
    arr_fenwick = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Array: {arr_fenwick}")

    fenwick = FenwickTree(arr_fenwick)
    print(f"Suma prefijo [0, 5]: {fenwick.consultar_prefijo(5)}")
    print(f"Suma rango [3, 7]: {fenwick.consultar_rango(3, 7)}")

    fenwick.actualizar(3, 6)
    print("Después de agregar 6 al índice 3:")
    print(f"  Valor en índice 3 (suma rango [3,3]): {fenwick.consultar_rango(3, 3)}")
    print(f"  Suma prefijo [0, 5]: {fenwick.consultar_prefijo(5)}")
