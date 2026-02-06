"""
14_Arboles - Árbol AVL (auto-balanceado)
=========================================
NodoAVL, ArbolAVL: inserción con rotaciones para mantener balance.
"""


class NodoAVL:
    """Nodo para árbol AVL."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    """Árbol AVL (balanceado)."""

    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        """Obtiene la altura de un nodo."""
        if nodo is None:
            return 0
        return nodo.altura

    def obtener_factor_balance(self, nodo):
        """Calcula el factor de balance."""
        if nodo is None:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, y):
        """Rotación a la derecha."""
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(
            self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)
        )
        x.altura = 1 + max(
            self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)
        )
        return x

    def rotar_izquierda(self, x):
        """Rotación a la izquierda."""
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(
            self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)
        )
        y.altura = 1 + max(
            self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)
        )
        return y

    def insertar(self, valor):
        """Inserta un valor manteniendo el balance."""
        self.raiz = self._insertar_avl(self.raiz, valor)

    def _insertar_avl(self, nodo, valor):
        """Inserta y balancea el árbol."""
        if nodo is None:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar_avl(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_avl(nodo.derecha, valor)

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha),
        )
        balance = self.obtener_factor_balance(nodo)

        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotar_derecha(nodo)
        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotar_izquierda(nodo)
        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)
        return nodo

    def inorden(self):
        """Recorrido inorden."""
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo:
            self._inorden_rec(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecha, resultado)


if __name__ == "__main__":
    print("=== Árbol AVL (auto-balanceado) ===\n")
    arbol = ArbolAVL()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)
    print("Inorden después de inserciones:", arbol.inorden())
    print("Nota: AVL mantiene balance; evita árboles degenerados (en lista).")
