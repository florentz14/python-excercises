# Archivo: 48_02_segment_tree.py
# Descripción: Segment Tree para consultas de rango

print("=== 2. Segment Tree ===\n")


class SegmentTree:
    """
    Segment Tree para consultas de rango.
    Complejidad: O(log n) consulta y actualización.
    """

    def __init__(self, arr, funcion=sum):
        self.n = len(arr)
        self.funcion = funcion
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.arbol = [0] * (2 * self.size)

        for i in range(self.n):
            self.arbol[self.size + i] = arr[i]

        if funcion == min:
            for i in range(self.size + self.n, 2 * self.size):
                self.arbol[i] = float('inf')

        for i in range(self.size - 1, 0, -1):
            self.arbol[i] = self._aplicar_funcion(
                self.arbol[2 * i],
                self.arbol[2 * i + 1]
            )

    def _aplicar_funcion(self, a, b):
        if self.funcion == sum:
            return a + b
        if self.funcion == min:
            return min(a, b)
        if self.funcion == max:
            return max(a, b)
        return self.funcion([a, b])

    def consultar_rango(self, l, r):
        """Consulta el rango [l, r) (l incluido, r excluido)."""
        l += self.size
        r += self.size
        resultado = 0 if self.funcion == sum else None
        if self.funcion == min:
            resultado = float('inf')
        elif self.funcion == max:
            resultado = float('-inf')

        while l < r:
            if l % 2 == 1:
                resultado = self._aplicar_funcion(resultado, self.arbol[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                resultado = self._aplicar_funcion(resultado, self.arbol[r])
            l //= 2
            r //= 2
        return resultado

    def actualizar(self, indice, valor):
        indice += self.size
        self.arbol[indice] = valor
        indice //= 2
        while indice >= 1:
            self.arbol[indice] = self._aplicar_funcion(
                self.arbol[2 * indice],
                self.arbol[2 * indice + 1]
            )
            indice //= 2


if __name__ == "__main__":
    arr_seg = [1, 3, 5, 7, 9, 11]
    print(f"Array: {arr_seg}")

    seg_tree_sum = SegmentTree(arr_seg, sum)
    print(f"Suma [1, 4): {seg_tree_sum.consultar_rango(1, 4)}")
    print(f"Suma [0, 6): {seg_tree_sum.consultar_rango(0, 6)}")

    seg_tree_min = SegmentTree(arr_seg, min)
    print(f"Mínimo [1, 4): {seg_tree_min.consultar_rango(1, 4)}")

    seg_tree_sum.actualizar(2, 10)
    print(f"Después de actualizar índice 2 a 10: {seg_tree_sum.consultar_rango(0, 6)}")
