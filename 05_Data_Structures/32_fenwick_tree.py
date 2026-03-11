# -------------------------------------------------
# File Name: 32_fenwick_tree.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Fenwick Tree (Binary Indexed Tree). Range sum queries and point updates. O(log n).
# -------------------------------------------------

print("=== 3. Fenwick Tree (Binary Indexed Tree) ===\n")


class FenwickTree:
    """
    Fenwick Tree for prefix sums.
    Complexity: O(log n) query and update.
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.arbol = [0] * (self.n + 1)
        for i in range(self.n):
            self.actualizar(i, arr[i])

    def _lsb(self, x):
        return x & -x

    def actualizar(self, index, delta):
        index += 1
        while index <= self.n:
            self.arbol[index] += delta
            index += self._lsb(index)

    def consultar_prefijo(self, index):
        index += 1
        suma = 0
        while index > 0:
            suma += self.arbol[index]
            index -= self._lsb(index)
        return suma

    def consultar_rango(self, l, r):
        """Sum of range [l, r] (inclusive)."""
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
    print("After adding 6 at index 3:")
    print(f"  Value at index 3 (range sum [3,3]): {fenwick.consultar_rango(3, 3)}")
    print(f"  Suma prefijo [0, 5]: {fenwick.consultar_prefijo(5)}")
