"""
14_Arboles - Operaciones comunes en árboles
===========================================
contar_hojas, sumar_valores, es_completo.
"""

from arbol_06_bst import ArbolBST


def contar_hojas(arbol):
    """Cuenta el número de hojas en un árbol binario."""
    def _contar_hojas(nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return _contar_hojas(nodo.izquierda) + _contar_hojas(nodo.derecha)

    return _contar_hojas(arbol.raiz)


def sumar_valores(arbol):
    """Suma todos los valores del árbol."""
    def _sumar(nodo):
        if nodo is None:
            return 0
        return nodo.valor + _sumar(nodo.izquierda) + _sumar(nodo.derecha)

    return _sumar(arbol.raiz)


def es_completo(arbol):
    """Verifica si el árbol binario está completo."""
    def _es_completo(nodo, indice, num_nodos):
        if nodo is None:
            return True
        if indice >= num_nodos:
            return False
        return _es_completo(
            nodo.izquierda, 2 * indice + 1, num_nodos
        ) and _es_completo(nodo.derecha, 2 * indice + 2, num_nodos)

    num_nodos = arbol.tamaño()
    return _es_completo(arbol.raiz, 0, num_nodos)


if __name__ == "__main__":
    print("=== Operaciones comunes ===\n")
    arbol = ArbolBST()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    print(f"Número de hojas: {contar_hojas(arbol)}")
    print(f"Suma de valores: {sumar_valores(arbol)}")
    print(f"Altura: {arbol.altura()}")
    print(f"Tamaño: {arbol.tamaño()}")
    print(f"¿Árbol completo? {es_completo(arbol)}")
